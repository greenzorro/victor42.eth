#!/usr/bin/env python3
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
import json
import ssl
import sys

# ================= Configuration =================
SITEMAP_URL = "https://victor42.eth.limo/sitemap.xml"
HOST = "victor42.eth.limo"
INDEXNOW_KEY = "bdc0773d573d420db7b46ef67e2329eb"
KEY_LOCATION = f"https://{HOST}/{INDEXNOW_KEY}.txt"
# Check files modified within this time window (e.g., last 24 hours)
TIME_WINDOW_HOURS = 24
# =================================================

def fetch_url(url, method="GET", data=None, headers=None):
    if headers is None:
        headers = {}
    
    ctx = ssl.create_default_context()

    req = urllib.request.Request(url, method=method, headers=headers)
    if data:
        req.data = data

    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as e:
        return e.code, e.reason
    except urllib.error.URLError as e:
        return 0, str(e.reason)
    except Exception as e:
        return 0, str(e)

def parse_iso_datetime(dt_str):
    # Standardize timezone format
    if dt_str.endswith('Z'):
        dt_str = dt_str[:-1] + '+00:00'
    # Parse ISO 8601
    try:
        return datetime.fromisoformat(dt_str)
    except Exception:
        # Fallback for simple date
        try:
            return datetime.strptime(dt_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except Exception:
            return None

def main():
    print(f"[{datetime.now()}] Starting IndexNow check...")
    
    # 1. Fetch live sitemap
    status, body = fetch_url(SITEMAP_URL)
    if status != 200:
        print(f"Error: Failed to fetch sitemap from {SITEMAP_URL} (Status {status})")
        return 1
        
    try:
        root = ET.fromstring(body)
    except Exception as e:
        print(f"Error: Failed to parse XML sitemap: {e}")
        return 1
        
    # XML namespace handling
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    now = datetime.now(timezone.utc)
    threshold = now - timedelta(hours=TIME_WINDOW_HOURS)
    
    recent_urls = []
    
    # 2. Extract and filter recent URLs
    for url_node in root.findall('ns:url', ns):
        loc_node = url_node.find('ns:loc', ns)
        lastmod_node = url_node.find('ns:lastmod', ns)
        
        if loc_node is not None and lastmod_node is not None:
            url = loc_node.text.strip()
            lastmod_str = lastmod_node.text.strip()
            
            lastmod_dt = parse_iso_datetime(lastmod_str)
            if lastmod_dt:
                # Compare timezone-aware datetimes
                if lastmod_dt.tzinfo is None:
                    lastmod_dt = lastmod_dt.replace(tzinfo=timezone.utc)
                
                if lastmod_dt >= threshold:
                    recent_urls.append(url)
                    
    if not recent_urls:
        print(f"No URLs modified in the last {TIME_WINDOW_HOURS} hours.")
        return 0
        
    print(f"Found {len(recent_urls)} recently modified URLs in sitemap:")
    for url in recent_urls:
        print(f" - {url}")
        
    # 3. Check if they return 200 OK (verifying IPNS propagation)
    live_urls = []
    for url in recent_urls:
        print(f"Verifying online status of {url}...")
        url_status, _ = fetch_url(url)
        if url_status == 200:
            print(f" -> Live (200 OK)")
            live_urls.append(url)
        else:
            print(f" -> Not live yet (Status: {url_status}). Skipping.")
            
    if not live_urls:
        print("None of the recently modified URLs are live yet. Exiting.")
        return 0
        
    # 4. Submit live URLs to IndexNow
    print(f"Submitting {len(live_urls)} live URLs to IndexNow...")
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": live_urls
    }
    
    json_data = json.dumps(payload).encode('utf-8')
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    
    indexnow_endpoint = "https://api.indexnow.org/indexnow"
    submit_status, response_body = fetch_url(indexnow_endpoint, method="POST", data=json_data, headers=headers)
    
    if submit_status == 200:
        print("Success: IndexNow notification sent successfully!")
        print(response_body.decode('utf-8', errors='ignore'))
        return 0
    else:
        print(f"Error: IndexNow submission failed with status {submit_status}")
        print(response_body.decode('utf-8', errors='ignore') if isinstance(response_body, bytes) else response_body)
        return 1

if __name__ == "__main__":
    sys.exit(main())
