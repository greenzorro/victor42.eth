#!/usr/bin/env python3
import argparse
import datetime as dt
import http.client
import json
import os
import urllib.parse


API_HOST = "api.4everland.dev"
PIN_NAME_PREFIX = "victor42.eth "


def require_env(name):
    value = os.environ.get(name)
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def api_request(token, method, path, query=None, body=None, timeout=60):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    payload = b""
    if body is not None:
        payload = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request_path = path
    if query:
        request_path = f"{path}?{urllib.parse.urlencode(query)}"

    conn = http.client.HTTPSConnection(API_HOST, timeout=timeout)
    conn.request(method, request_path, body=payload, headers=headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    parsed = json.loads(data.decode("utf-8")) if data else {}
    if response.status >= 300:
        raise SystemExit(f"4EVER Pin API failed: {response.status} {response.reason}\n{parsed}")
    return parsed


def parse_timestamp(value):
    if not value:
        return dt.datetime.min.replace(tzinfo=dt.UTC)
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def pin_cid(token, cid, name):
    return api_request(
        token,
        "POST",
        "/pins",
        body={
            "cid": cid,
            "name": name,
        },
    )


def list_workflow_pins(token):
    pins = []
    after = None

    while True:
        query = {"limit": 100}
        if after:
            query["after"] = after

        payload = api_request(token, "GET", "/pins", query=query)
        results = payload.get("results", [])
        for item in results:
            pin = item.get("pin") or {}
            name = pin.get("name") or ""
            if name.startswith(PIN_NAME_PREFIX):
                pins.append(item)

        if len(results) < query["limit"]:
            break
        after = results[-1].get("created")
        if not after:
            break

    return pins


def find_existing_workflow_pin(pins, cid):
    for item in pins:
        pin = item.get("pin") or {}
        if pin.get("cid") == cid:
            return item
    return None


def delete_pins(token, request_ids):
    for request_id in request_ids:
        api_request(token, "DELETE", f"/pins/{urllib.parse.quote(request_id, safe='')}")


def cleanup_old_pins(token, current_cid, keep, dry_run):
    if keep < 1:
        raise SystemExit("--retention-keep must be at least 1")

    pins = sorted(
        list_workflow_pins(token),
        key=lambda item: parse_timestamp(item.get("created")),
        reverse=True,
    )
    keep_ids = {item["requestid"] for item in pins[:keep] if item.get("requestid")}
    keep_ids.update(
        item["requestid"]
        for item in pins
        if item.get("requestid") and (item.get("pin") or {}).get("cid") == current_cid
    )
    delete_candidates = [item for item in pins if item.get("requestid") not in keep_ids]

    print(f"FOUREVERLAND_RETENTION_TOTAL={len(pins)}")
    print(f"FOUREVERLAND_RETENTION_KEEP={len(keep_ids)}")
    print(f"FOUREVERLAND_RETENTION_DELETE={len(delete_candidates)}")
    if not delete_candidates:
        return

    for item in delete_candidates:
        pin = item.get("pin") or {}
        print(f"FOUREVERLAND_RETENTION_DELETE_CANDIDATE={item.get('requestid')} cid={pin.get('cid')}")

    if dry_run:
        print("FOUREVERLAND_RETENTION_DRY_RUN=true")
        return

    delete_pins(token, [item["requestid"] for item in delete_candidates if item.get("requestid")])
    print("FOUREVERLAND_RETENTION_DRY_RUN=false")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cid", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--retention-keep", type=int, default=20)
    parser.add_argument("--retention-dry-run", action="store_true")
    args = parser.parse_args()

    token = require_env("FOUREVERLAND_TOKEN")
    existing_pins = list_workflow_pins(token)
    pin = find_existing_workflow_pin(existing_pins, args.cid)
    if pin:
        print("FOUREVERLAND_PIN_SKIPPED=already pinned by workflow")
    else:
        pin = pin_cid(token, args.cid, args.name)
    print(f"FOUREVERLAND_PIN_REQUEST_ID={pin.get('requestid')}")
    print(f"FOUREVERLAND_PIN_STATUS={pin.get('status')}")
    print(f"FOUREVERLAND_PIN_CID={(pin.get('pin') or {}).get('cid')}")

    cleanup_old_pins(token, args.cid, args.retention_keep, args.retention_dry_run)


if __name__ == "__main__":
    main()
