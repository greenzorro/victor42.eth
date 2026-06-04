#!/usr/bin/env python3
import argparse

from filebase_client import delete_release_objects, list_release_objects, require_env


def cleanup_old_releases(access_key, secret_key, bucket, prefix, keep, current_key, dry_run):
    if keep < 1:
        raise SystemExit("--keep must be at least 1")

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--current-object-key", required=True)
    parser.add_argument("--keep", type=int, default=20)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    access_key = require_env("FILEBASE_ACCESS_KEY")
    secret_key = require_env("FILEBASE_SECRET_KEY")
    bucket = require_env("FILEBASE_BUCKET")

    cleanup_old_releases(
        access_key,
        secret_key,
        bucket,
        args.prefix,
        args.keep,
        args.current_object_key,
        args.dry_run,
    )


if __name__ == "__main__":
    main()
