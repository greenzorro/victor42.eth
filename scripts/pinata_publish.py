#!/usr/bin/env python3
import argparse
import datetime as dt
import http.client
import json
import os
import urllib.parse


PINATA_HOST = "api.pinata.cloud"
PINATA_SOURCE = "victor42-eth-ipfs-workflow"


def require_env(name):
    value = os.environ.get(name)
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def pinata_request(jwt, method, path, query=None, body=None, timeout=60):
    headers = {
        "Authorization": f"Bearer {jwt}",
    }
    payload = b""
    if body is not None:
        payload = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request_path = path
    if query:
        request_path = f"{path}?{urllib.parse.urlencode(query)}"

    conn = http.client.HTTPSConnection(PINATA_HOST, timeout=timeout)
    conn.request(method, request_path, body=payload, headers=headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    parsed = json.loads(data.decode("utf-8")) if data else {}
    if response.status >= 300:
        raise SystemExit(f"Pinata API failed: {response.status} {response.reason}\n{parsed}")
    return parsed


def pin_cid(jwt, cid, name):
    return pinata_request(
        jwt,
        "POST",
        "/pinning/pinByHash",
        body={
            "hashToPin": cid,
            "pinataMetadata": {
                "name": name,
                "keyvalues": {
                    "source": PINATA_SOURCE,
                },
            },
        },
    )


def parse_pinata_timestamp(value):
    if not value:
        return dt.datetime.min.replace(tzinfo=dt.UTC)
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def list_workflow_pins(jwt):
    pins = []
    page_offset = 0

    while True:
        query = {
            "status": "pinned",
            "pageLimit": 100,
            "pageOffset": page_offset,
        }

        payload = pinata_request(jwt, "GET", "/data/pinList", query=query)
        files = payload.get("rows", [])
        for item in files:
            metadata = item.get("metadata") or {}
            keyvalues = metadata.get("keyvalues") or {}
            if keyvalues.get("source") == PINATA_SOURCE:
                pins.append(item)

        if len(files) < query["pageLimit"]:
            break
        page_offset += query["pageLimit"]

    return pins


def delete_pinata_files(jwt, file_ids):
    for cid in file_ids:
        pinata_request(jwt, "DELETE", f"/pinning/unpin/{urllib.parse.quote(cid, safe='')}")


def cleanup_old_pins(jwt, current_cid, keep, dry_run):
    if keep < 1:
        raise SystemExit("--retention-keep must be at least 1")

    pins = sorted(
        list_workflow_pins(jwt),
        key=lambda item: parse_pinata_timestamp(item.get("date_pinned")),
        reverse=True,
    )
    keep_cids = {item["ipfs_pin_hash"] for item in pins[:keep] if item.get("ipfs_pin_hash")}
    keep_cids.add(current_cid)
    delete_candidates = [item for item in pins if item.get("ipfs_pin_hash") not in keep_cids]

    print(f"PINATA_RETENTION_TOTAL={len(pins)}")
    print(f"PINATA_RETENTION_KEEP={len(keep_cids)}")
    print(f"PINATA_RETENTION_DELETE={len(delete_candidates)}")
    if not delete_candidates:
        return

    for item in delete_candidates:
        print(f"PINATA_RETENTION_DELETE_CANDIDATE={item.get('ipfs_pin_hash')}")

    if dry_run:
        print("PINATA_RETENTION_DRY_RUN=true")
        return

    delete_pinata_files(jwt, [item["ipfs_pin_hash"] for item in delete_candidates if item.get("ipfs_pin_hash")])
    print("PINATA_RETENTION_DRY_RUN=false")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cid", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--retention-keep", type=int, default=20)
    parser.add_argument("--retention-dry-run", action="store_true")
    args = parser.parse_args()

    jwt = require_env("PINATA_JWT")
    pin = pin_cid(jwt, args.cid, args.name)
    print(f"PINATA_PIN_ID={pin.get('id')}")
    print(f"PINATA_PIN_CID={pin.get('ipfsHash')}")
    print(f"PINATA_PIN_STATUS={pin.get('status')}")

    cleanup_old_pins(jwt, args.cid, args.retention_keep, args.retention_dry_run)


if __name__ == "__main__":
    main()
