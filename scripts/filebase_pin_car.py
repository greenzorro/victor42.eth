#!/usr/bin/env python3
import argparse

from filebase_client import put_car, require_env


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--car", required=True)
    parser.add_argument("--object-key", required=True)
    parser.add_argument("--expected-cid", required=True)
    args = parser.parse_args()

    access_key = require_env("FILEBASE_ACCESS_KEY")
    secret_key = require_env("FILEBASE_SECRET_KEY")
    bucket = require_env("FILEBASE_BUCKET")

    cid = put_car(access_key, secret_key, bucket, args.object_key, args.car)
    if cid != args.expected_cid:
        raise SystemExit(f"Filebase returned CID {cid}, expected {args.expected_cid}")

    print(f"FILEBASE_CID={cid}")
    print(f"FILEBASE_OBJECT_KEY={args.object_key}")


if __name__ == "__main__":
    main()
