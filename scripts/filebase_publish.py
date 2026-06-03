#!/usr/bin/env python3
import argparse
import base64
import datetime as dt
import hashlib
import hmac
import http.client
import json
import os
import pathlib
import urllib.parse
import xml.etree.ElementTree as ET


S3_HOST = "s3.filebase.com"
S3_REGION = "us-east-1"
S3_SERVICE = "s3"
API_HOST = "api.filebase.io"
PINATA_HOST = "api.pinata.cloud"
S3_NS = "http://s3.amazonaws.com/doc/2006-03-01/"


def require_env(name):
    value = os.environ.get(name)
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def signing_key(secret_key, date_stamp):
    key_date = sign(("AWS4" + secret_key).encode("utf-8"), date_stamp)
    key_region = sign(key_date, S3_REGION)
    key_service = sign(key_region, S3_SERVICE)
    return sign(key_service, "aws4_request")


def canonical_query_string(query):
    encoded = [
        (
            urllib.parse.quote(str(key), safe="-_.~"),
            urllib.parse.quote(str(value), safe="-_.~"),
        )
        for key, value in query
    ]
    return "&".join(f"{key}={value}" for key, value in sorted(encoded))


def s3_request(access_key, secret_key, method, path, query=None, body=b"", headers=None, timeout=60):
    query = query or []
    headers = {k.lower(): v for k, v in (headers or {}).items()}
    now = dt.datetime.now(dt.UTC)
    amz_date = now.strftime("%Y%m%dT%H%M%SZ")
    date_stamp = now.strftime("%Y%m%d")
    payload_hash = hashlib.sha256(body).hexdigest()

    headers["host"] = S3_HOST
    headers["x-amz-content-sha256"] = payload_hash
    headers["x-amz-date"] = amz_date

    sorted_headers = sorted(headers.items())
    canonical_headers = "".join(f"{k}:{v}\n" for k, v in sorted_headers)
    signed_headers = ";".join(k for k, _ in sorted_headers)
    canonical_query = canonical_query_string(query)
    canonical_request = "\n".join(
        [
            method,
            path,
            canonical_query,
            canonical_headers,
            signed_headers,
            payload_hash,
        ]
    )
    credential_scope = f"{date_stamp}/{S3_REGION}/{S3_SERVICE}/aws4_request"
    string_to_sign = "\n".join(
        [
            "AWS4-HMAC-SHA256",
            amz_date,
            credential_scope,
            hashlib.sha256(canonical_request.encode("utf-8")).hexdigest(),
        ]
    )
    signature = hmac.new(
        signing_key(secret_key, date_stamp),
        string_to_sign.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    headers["Authorization"] = (
        "AWS4-HMAC-SHA256 "
        f"Credential={access_key}/{credential_scope}, "
        f"SignedHeaders={signed_headers}, "
        f"Signature={signature}"
    )

    request_path = path
    if canonical_query:
        request_path = f"{path}?{canonical_query}"
    conn = http.client.HTTPSConnection(S3_HOST, timeout=timeout)
    conn.request(method, request_path, body=body, headers=headers)
    response = conn.getresponse()
    data = response.read()
    response_headers = {k.lower(): v for k, v in response.getheaders()}
    conn.close()
    return response.status, response.reason, response_headers, data


def s3_put_car(access_key, secret_key, bucket, object_key, car_path):
    body = pathlib.Path(car_path).read_bytes()
    path = f"/{bucket}/{urllib.parse.quote(object_key, safe='/-_.~')}"
    headers = {
        "content-type": "application/vnd.ipld.car",
        "x-amz-meta-import": "car",
    }

    status, reason, response_headers, data = s3_request(
        access_key,
        secret_key,
        "PUT",
        path,
        body=body,
        headers=headers,
        timeout=300,
    )
    if status >= 300:
        raise SystemExit(f"Filebase S3 upload failed: {status} {reason}\n{data.decode(errors='replace')}")
    cid = response_headers.get("x-amz-meta-cid")
    if not cid:
        raise SystemExit("Filebase S3 upload succeeded but x-amz-meta-cid header was missing")
    return cid


def parse_s3_timestamp(value):
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def list_release_objects(access_key, secret_key, bucket, prefix):
    path = f"/{bucket}"
    token = None
    objects = []

    while True:
        query = [("list-type", "2"), ("prefix", prefix)]
        if token:
            query.append(("continuation-token", token))

        status, reason, _, data = s3_request(access_key, secret_key, "GET", path, query=query)
        if status >= 300:
            raise SystemExit(f"Filebase S3 list failed: {status} {reason}\n{data.decode(errors='replace')}")

        root = ET.fromstring(data)
        for item in root.findall(f"{{{S3_NS}}}Contents"):
            key = item.findtext(f"{{{S3_NS}}}Key")
            modified = item.findtext(f"{{{S3_NS}}}LastModified")
            size = item.findtext(f"{{{S3_NS}}}Size")
            if key and key.startswith(prefix) and key.removeprefix(prefix).startswith("site-") and key.endswith(".car"):
                objects.append(
                    {
                        "key": key,
                        "last_modified": parse_s3_timestamp(modified),
                        "size": int(size or 0),
                    }
                )

        if root.findtext(f"{{{S3_NS}}}IsTruncated") != "true":
            break
        token = root.findtext(f"{{{S3_NS}}}NextContinuationToken")
        if not token:
            break

    return objects


def delete_release_objects(access_key, secret_key, bucket, keys):
    path = f"/{bucket}"
    for start in range(0, len(keys), 1000):
        chunk = keys[start : start + 1000]
        root = ET.Element("Delete")
        ET.SubElement(root, "Quiet").text = "true"
        for key in chunk:
            obj = ET.SubElement(root, "Object")
            ET.SubElement(obj, "Key").text = key
        body = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        content_md5 = base64.b64encode(hashlib.md5(body).digest()).decode("ascii")
        headers = {
            "content-md5": content_md5,
            "content-type": "application/xml",
        }
        status, reason, _, data = s3_request(
            access_key,
            secret_key,
            "POST",
            path,
            query=[("delete", "")],
            body=body,
            headers=headers,
        )
        if status >= 300:
            raise SystemExit(f"Filebase S3 delete failed: {status} {reason}\n{data.decode(errors='replace')}")


def cleanup_old_releases(access_key, secret_key, bucket, prefix, keep, current_key, dry_run):
    if keep < 1:
        raise SystemExit("--retention-keep must be at least 1")

    objects = sorted(
        list_release_objects(access_key, secret_key, bucket, prefix),
        key=lambda item: item["last_modified"],
        reverse=True,
    )
    keep_keys = {item["key"] for item in objects[:keep]}
    keep_keys.add(current_key)
    delete_candidates = [item for item in objects if item["key"] not in keep_keys]

    print(f"FILEBASE_RETENTION_TOTAL={len(objects)}")
    print(f"FILEBASE_RETENTION_KEEP={len(keep_keys)}")
    print(f"FILEBASE_RETENTION_DELETE={len(delete_candidates)}")
    if not delete_candidates:
        return

    for item in delete_candidates:
        print(f"FILEBASE_RETENTION_DELETE_CANDIDATE={item['key']} size={item['size']}")

    if dry_run:
        print("FILEBASE_RETENTION_DRY_RUN=true")
        return

    delete_release_objects(access_key, secret_key, bucket, [item["key"] for item in delete_candidates])
    print("FILEBASE_RETENTION_DRY_RUN=false")


def update_ipns(access_key, secret_key, label, cid):
    auth = base64.b64encode(f"{access_key}:{secret_key}".encode("utf-8")).decode("ascii")
    body = json.dumps({"cid": cid}).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {auth}",
        "Content-Type": "application/json",
    }
    conn = http.client.HTTPSConnection(API_HOST, timeout=60)
    conn.request("PUT", f"/v1/names/{urllib.parse.quote(label, safe='')}", body=body, headers=headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    payload = json.loads(data.decode("utf-8")) if data else {}
    if response.status >= 300:
        raise SystemExit(f"Filebase IPNS update failed: {response.status} {response.reason}\n{payload}")
    return payload


def pinata_pin_cid(jwt, cid, name):
    body = json.dumps(
        {
            "hashToPin": cid,
            "pinataMetadata": {
                "name": name,
                "keyvalues": {
                    "source": "filebase-ipns-workflow",
                },
            },
        }
    ).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
    }
    conn = http.client.HTTPSConnection(PINATA_HOST, timeout=60)
    conn.request("POST", "/pinning/pinByHash", body=body, headers=headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    payload = json.loads(data.decode("utf-8")) if data else {}
    if response.status >= 300:
        raise SystemExit(f"Pinata pin-by-CID failed: {response.status} {response.reason}\n{payload}")
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--car", required=True)
    parser.add_argument("--object-key", required=True)
    parser.add_argument("--retention-prefix")
    parser.add_argument("--retention-keep", type=int, default=20)
    parser.add_argument("--retention-dry-run", action="store_true")
    args = parser.parse_args()

    access_key = require_env("FILEBASE_ACCESS_KEY")
    secret_key = require_env("FILEBASE_SECRET_KEY")
    bucket = require_env("FILEBASE_BUCKET")
    ipns_label = require_env("FILEBASE_IPNS_NAME")

    cid = s3_put_car(access_key, secret_key, bucket, args.object_key, args.car)
    ipns = update_ipns(access_key, secret_key, ipns_label, cid)
    network_key = ipns.get("network_key")

    print(f"FILEBASE_CID={cid}")
    if network_key:
        print(f"FILEBASE_IPNS_KEY={network_key}")
        print(f"FILEBASE_IPNS_URL=https://ipfs.io/ipns/{network_key}/")

    pinata_jwt = os.environ.get("PINATA_JWT")
    if pinata_jwt:
        pinata = pinata_pin_cid(pinata_jwt, cid, f"victor42.eth {args.object_key}")
        print(f"PINATA_PIN_ID={pinata.get('id')}")
        print(f"PINATA_PIN_CID={pinata.get('ipfsHash')}")
        print(f"PINATA_PIN_STATUS={pinata.get('status')}")
    else:
        print("PINATA_PIN_SKIPPED=missing PINATA_JWT")

    if args.retention_prefix:
        cleanup_old_releases(
            access_key,
            secret_key,
            bucket,
            args.retention_prefix,
            args.retention_keep,
            args.object_key,
            args.retention_dry_run,
        )


if __name__ == "__main__":
    main()
