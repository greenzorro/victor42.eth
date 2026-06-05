#!/usr/bin/env python3
import argparse

from foureverland_client import (
    delete_pins,
    find_existing_workflow_pin,
    list_workflow_pins,
    parse_timestamp,
    pin_cid,
    require_env,
)


def cleanup_old_pins(pins, token, current_cid, keep, dry_run):
    if keep < 1:
        raise SystemExit("--keep must be at least 1")

    pins = sorted(
        pins,
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
    parser.add_argument("--keep", type=int, default=20)
    parser.add_argument("--dry-run-retention", action="store_true")
    args = parser.parse_args()

    token = require_env("FOUREVERLAND_TOKEN")
    existing_pins = list_workflow_pins(token)
    pin = find_existing_workflow_pin(existing_pins, args.cid)
    if pin:
        print("FOUREVERLAND_PIN_SKIPPED=already pinned by workflow")
    else:
        pin = pin_cid(token, args.cid, args.name)
        existing_pins = list_workflow_pins(token)
    print(f"FOUREVERLAND_PIN_REQUEST_ID={pin.get('requestid')}")
    print(f"FOUREVERLAND_PIN_STATUS={pin.get('status')}")
    print(f"FOUREVERLAND_PIN_CID={(pin.get('pin') or {}).get('cid')}")
    cleanup_old_pins(existing_pins, token, args.cid, args.keep, args.dry_run_retention)


if __name__ == "__main__":
    main()
