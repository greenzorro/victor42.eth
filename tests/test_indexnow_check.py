import sys
from pathlib import Path
from unittest.mock import patch


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import indexnow_check


# ==================== parse_iso_datetime 纯函数测试 ====================

def test_parse_iso_datetime_with_z_suffix():
    """Z 后缀应转为 UTC +00:00 并正确解析"""
    dt = indexnow_check.parse_iso_datetime("2026-07-30T12:00:00Z")
    assert dt is not None
    assert dt.year == 2026 and dt.month == 7 and dt.day == 30
    assert dt.utcoffset().total_seconds() == 0  # Z → UTC


def test_parse_iso_datetime_with_explicit_offset():
    """带显式时区偏移的 ISO 字符串"""
    dt = indexnow_check.parse_iso_datetime("2026-07-30T12:00:00+08:00")
    assert dt is not None
    assert dt.utcoffset().total_seconds() == 8 * 3600


def test_parse_iso_datetime_simple_date_naive():
    """纯日期字符串（无时区）走 fromisoformat，返回 naive datetime。
    main() 在比较前会补 UTC（见 lastmod_dt.tzinfo is None 分支）。
    fallback 分支（strptime + replace(UTC)）仅在 fromisoformat 失败时触发，
    本测试同时锁死这条不变量：纯日期不应触发 fallback。
    """
    dt = indexnow_check.parse_iso_datetime("2026-07-30")
    assert dt is not None
    assert dt.year == 2026 and dt.month == 7 and dt.day == 30
    assert dt.tzinfo is None  # naive；由 main() 补 UTC


def test_parse_iso_datetime_invalid_returns_none():
    """无效字符串应返回 None（业务逻辑依赖此判定跳过）"""
    assert indexnow_check.parse_iso_datetime("not-a-date") is None
    assert indexnow_check.parse_iso_datetime("") is None


# ==================== main() 集成路径测试 ====================

def test_sitemap_fetch_failure_returns_error():
    with patch.object(indexnow_check, "fetch_url", return_value=(503, b"unavailable")):
        assert indexnow_check.main() == 1


def test_invalid_sitemap_returns_error():
    with patch.object(indexnow_check, "fetch_url", return_value=(200, b"not xml")):
        assert indexnow_check.main() == 1


def test_no_recent_urls_is_successful_noop(capsys):
    """旧 URL（2000 年）应被时间过滤排除，返回 0 且不进入存活检查"""
    sitemap = b"""<?xml version='1.0'?>
    <urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>
      <url><loc>https://victor42.eth.limo/old</loc><lastmod>2000-01-01</lastmod></url>
    </urlset>"""
    with patch.object(indexnow_check, "fetch_url", return_value=(200, sitemap)):
        assert indexnow_check.main() == 0
    out = capsys.readouterr().out
    # 语义验证：确实因"近期无 URL"而退出，而不是因其他原因返回 0
    assert "No URLs modified" in out
    # 关键：旧 URL 不该进入存活检查流程
    assert "Verifying online status" not in out


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


def test_successful_submission_returns_zero(capsys):
    """Happy path：近期 URL + 存活 + IndexNow 提交成功 → 返回 0"""
    sitemap = b"""<?xml version='1.0'?>
    <urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>
      <url><loc>https://victor42.eth.limo/new</loc><lastmod>2099-01-01</lastmod></url>
    </urlset>"""
    responses = [
        (200, sitemap),         # sitemap fetch
        (200, b"live"),         # URL liveness check
        (200, b'{"ok":true}'),  # IndexNow submission success
    ]
    with patch.object(indexnow_check, "fetch_url", side_effect=responses):
        assert indexnow_check.main() == 0
    out = capsys.readouterr().out
    assert "Success" in out
