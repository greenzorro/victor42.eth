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


S3_HOST = "s3.filebase.com"
S3_REGION = "us-east-1"
S3_SERVICE = "s3"
API_HOST = "api.filebase.io"


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


def s3_put_car(access_key, secret_key, bucket, object_key, car_path):
    body = pathlib.Path(car_path).read_bytes()
    now = dt.datetime.now(dt.UTC)
    amz_date = now.strftime("%Y%m%dT%H%M%SZ")
    date_stamp = now.strftime("%Y%m%d")
    payload_hash = hashlib.sha256(body).hexdigest()
    path = f"/{bucket}/{urllib.parse.quote(object_key, safe='/-_.~')}"

    headers = {
        "content-type": "application/vnd.ipld.car",
        "host": S3_HOST,
        "x-amz-content-sha256": payload_hash,
        "x-amz-date": amz_date,
        "x-amz-meta-import": "car",
    }
    sorted_headers = sorted(headers.items())
    canonical_headers = "".join(f"{k}:{v}\n" for k, v in sorted_headers)
    signed_headers = ";".join(k for k, _ in sorted_headers)
    canonical_request = "\n".join(
        [
            "PUT",
            urllib.parse.quote(path, safe="/-_.~"),
            "",
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

    conn = http.client.HTTPSConnection(S3_HOST, timeout=300)
    conn.request("PUT", path, body=body, headers=headers)
    response = conn.getresponse()
    data = response.read()
    response_headers = {k.lower(): v for k, v in response.getheaders()}
    conn.close()
    if response.status >= 300:
        raise SystemExit(f"Filebase S3 upload failed: {response.status} {response.reason}\n{data.decode(errors='replace')}")
    cid = response_headers.get("x-amz-meta-cid")
    if not cid:
        raise SystemExit("Filebase S3 upload succeeded but x-amz-meta-cid header was missing")
    return cid


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--car", required=True)
    parser.add_argument("--object-key", required=True)
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


if __name__ == "__main__":
    main()
