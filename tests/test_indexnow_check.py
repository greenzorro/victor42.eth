import sys
from pathlib import Path
from unittest.mock import patch


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import indexnow_check


def test_sitemap_fetch_failure_returns_error():
    with patch.object(indexnow_check, "fetch_url", return_value=(503, b"unavailable")):
        assert indexnow_check.main() == 1


def test_invalid_sitemap_returns_error():
    with patch.object(indexnow_check, "fetch_url", return_value=(200, b"not xml")):
        assert indexnow_check.main() == 1


def test_no_recent_urls_is_successful_noop():
    sitemap = b"""<?xml version='1.0'?>
    <urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>
      <url><loc>https://victor42.eth.limo/old</loc><lastmod>2000-01-01</lastmod></url>
    </urlset>"""
    with patch.object(indexnow_check, "fetch_url", return_value=(200, sitemap)):
        assert indexnow_check.main() == 0


def test_indexnow_submission_failure_returns_error():
    sitemap = b"""<?xml version='1.0'?>
    <urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>
      <url><loc>https://victor42.eth.limo/new</loc><lastmod>2099-01-01</lastmod></url>
    </urlset>"""
    responses = [
        (200, sitemap),
        (200, b"live"),
        (500, b"submission failed"),
    ]
    with patch.object(indexnow_check, "fetch_url", side_effect=responses):
        assert indexnow_check.main() == 1
