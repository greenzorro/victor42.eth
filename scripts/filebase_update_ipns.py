#!/usr/bin/env python3
import argparse

from filebase_client import require_env, update_ipns


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cid", required=True)
    args = parser.parse_args()

    access_key = require_env("FILEBASE_ACCESS_KEY")
    secret_key = require_env("FILEBASE_SECRET_KEY")
    ipns_label = require_env("FILEBASE_IPNS_NAME")

    payload = update_ipns(access_key, secret_key, ipns_label, args.cid)
    network_key = payload.get("network_key")

    print(f"FILEBASE_IPNS_CID={args.cid}")
    if network_key:
        print(f"FILEBASE_IPNS_KEY={network_key}")
        print(f"FILEBASE_IPNS_URL=https://ipfs.io/ipns/{network_key}/")


if __name__ == "__main__":
    main()
