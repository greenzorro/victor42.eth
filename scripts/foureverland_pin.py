#!/usr/bin/env python3
import argparse

from foureverland_client import find_existing_workflow_pin, list_workflow_pins, pin_cid, require_env


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cid", required=True)
    parser.add_argument("--name", required=True)
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


if __name__ == "__main__":
    main()
