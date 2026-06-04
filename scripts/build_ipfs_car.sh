#!/usr/bin/env bash
set -euo pipefail

source_dir="${1:-public}"
car_path="${2:-dist/site.car}"
cid_path="${3:-dist/root.cid}"
ipfs_car_package="${IPFS_CAR_PACKAGE:-ipfs-car@3.1.0}"

if [[ ! -d "$source_dir" ]]; then
  echo "Source directory does not exist: $source_dir" >&2
  exit 1
fi

if [[ ! -f "$source_dir/index.html" ]]; then
  echo "Source directory is missing index.html: $source_dir" >&2
  exit 1
fi

mkdir -p "$(dirname "$car_path")" "$(dirname "$cid_path")"

root_cid="$(npx --yes "$ipfs_car_package" pack "$source_dir" --output "$car_path" | tail -n 1)"
if [[ -z "$root_cid" ]]; then
  echo "ipfs-car did not return a root CID" >&2
  exit 1
fi

printf '%s\n' "$root_cid" > "$cid_path"
printf 'ROOT_CID=%s\n' "$root_cid"

if [[ -n "${GITHUB_OUTPUT:-}" ]]; then
  printf 'ROOT_CID=%s\n' "$root_cid" >> "$GITHUB_OUTPUT"
fi
