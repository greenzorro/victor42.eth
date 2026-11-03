"""
Locks the CAR build contract implemented by scripts/build_car.mjs.

Contracts covered:
- A site directory becomes a single CAR plus a root CID file.
- Root CID is CIDv1 dag-pb (a directory node, not a bare file).
- Same input produces the same root CID (content addressing, no timestamps).
- Hidden files are packed (unlike some legacy packers that skip dotfiles).
- Missing index.html / missing source directory fail fast with exit code 1.
- GITHUB_OUTPUT receives the ROOT_CID line consumed by the publish workflow.
"""
import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
BUILD_CAR = ROOT / "scripts" / "build_car.mjs"

pytestmark = pytest.mark.skipif(
    shutil.which("node") is None or not (ROOT / "node_modules").is_dir(),
    reason="needs node and `npm ci` deps installed",
)


def run_build(source, car, cid, env=None):
    cmd = ["node", str(BUILD_CAR), str(source), str(car), str(cid)]
    return subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=ROOT)


def make_site(base: Path, files: dict) -> Path:
    site = base / "public"
    for name, content in files.items():
        path = site / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            path.write_bytes(content)
        else:
            path.write_text(content)
    return site


def car_roots(car_path: Path):
    """Read roots back with an independent implementation (@ipld/car)."""
    script = (
        "import('@ipld/car').then(async ({CarReader}) => {"
        f"  const reader = await CarReader.fromIterable(await import('node:fs').then"
        f"(fs => fs.createReadStream({json.dumps(str(car_path))})));"
        "  const roots = await reader.getRoots();"
        "  const blocks = [];"
        "  for await (const block of reader.blocks()) blocks.push(String(block.cid));"
        "  console.log(JSON.stringify({roots: roots.map(String), blocks: blocks.length}));"
        "}).catch(e => { console.error(e.message); process.exit(1); });"
    )
    result = subprocess.run(
        ["node", "-e", script], capture_output=True, text=True, cwd=ROOT
    )
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def test_packs_directory_into_car_with_directory_root(tmp_path):
    """Root must be a dag-pb directory (bafybei…), not a raw/file node (bafkrei…)."""
    site = make_site(tmp_path, {"index.html": "<html>hi</html>", "post/a.md": "a"})
    result = run_build(site, tmp_path / "site.car", tmp_path / "root.cid")

    assert result.returncode == 0, result.stderr
    root_cid = (tmp_path / "root.cid").read_text().strip()
    assert root_cid.startswith("bafybei"), root_cid
    assert f"ROOT_CID={root_cid}" in result.stdout

    parsed = car_roots(tmp_path / "site.car")
    assert parsed["roots"] == [root_cid]
    # index.html + post/a.md + dir(post) + dir(root)
    assert parsed["blocks"] == 4


def test_same_input_yields_same_root_cid(tmp_path):
    """Content addressing: identical trees must produce identical roots."""
    files = {"index.html": "<html>x</html>", "a.txt": "a", "deep/b.txt": "b"}
    site = make_site(tmp_path, files)

    run_build(site, tmp_path / "one.car", tmp_path / "one.cid")
    run_build(site, tmp_path / "two.car", tmp_path / "two.cid")

    assert (tmp_path / "one.cid").read_text() == (tmp_path / "two.cid").read_text()


def test_multichunk_file_changes_root(tmp_path):
    """Files above the 1 MiB chunk size are split, and the root reflects content."""
    site = make_site(tmp_path, {"index.html": "<html>x</html>"})
    run_build(site, tmp_path / "small.car", tmp_path / "small.cid")

    (site / "big.bin").write_bytes(b"\0" * (1024 * 1024 + 1))
    run_build(site, tmp_path / "big.car", tmp_path / "big.cid")

    assert (tmp_path / "small.cid").read_text() != (tmp_path / "big.cid").read_text()
    assert car_roots(tmp_path / "big.car")["blocks"] > car_roots(tmp_path / "small.car")["blocks"]


def test_hidden_files_are_packed(tmp_path):
    """Dotfiles are part of the site (e.g. .well-known/) and must not be dropped."""
    site = make_site(tmp_path, {"index.html": "<html>x</html>"})
    run_build(site, tmp_path / "plain.car", tmp_path / "plain.cid")

    (site / ".well-known").mkdir()
    (site / ".well-known" / "security.txt").write_text("Contact: mailto:hi@victor42.work\n")
    run_build(site, tmp_path / "hidden.car", tmp_path / "hidden.cid")

    assert (tmp_path / "plain.cid").read_text() != (tmp_path / "hidden.cid").read_text()


def test_missing_index_html_fails(tmp_path):
    site = make_site(tmp_path, {"a.txt": "a"})
    result = run_build(site, tmp_path / "site.car", tmp_path / "root.cid")

    assert result.returncode == 1
    assert "missing index.html" in result.stderr


def test_missing_source_dir_fails(tmp_path):
    result = run_build(tmp_path / "nope", tmp_path / "site.car", tmp_path / "root.cid")

    assert result.returncode == 1
    assert "Source directory does not exist" in result.stderr


def test_writes_root_cid_to_github_output(tmp_path):
    """The publish workflow reads steps.car.outputs.ROOT_CID from GITHUB_OUTPUT."""
    site = make_site(tmp_path, {"index.html": "<html>x</html>"})
    gh_output = tmp_path / "gh_output"
    env = {**os.environ, "GITHUB_OUTPUT": str(gh_output)}

    result = run_build(site, tmp_path / "site.car", tmp_path / "root.cid", env=env)

    assert result.returncode == 0, result.stderr
    assert gh_output.read_text().strip() == f"ROOT_CID={(tmp_path / 'root.cid').read_text().strip()}"
