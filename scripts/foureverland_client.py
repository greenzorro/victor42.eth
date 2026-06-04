#!/usr/bin/env python3
import datetime as dt
import http.client
import json
import os
import urllib.parse


API_HOST = "api.4everland.dev"
PIN_NAME_PREFIX = "victor42.eth "


def require_env(name):
    value = os.environ.get(name)
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def api_request(token, method, path, query=None, body=None, timeout=60):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    payload = b""
    if body is not None:
        payload = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request_path = path
    if query:
        request_path = f"{path}?{urllib.parse.urlencode(query)}"

    conn = http.client.HTTPSConnection(API_HOST, timeout=timeout)
    conn.request(method, request_path, body=payload, headers=headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    parsed = json.loads(data.decode("utf-8")) if data else {}
    if response.status >= 300:
        raise SystemExit(f"4EVER Pin API failed: {response.status} {response.reason}\n{parsed}")
    return parsed


def parse_timestamp(value):
    if not value:
        return dt.datetime.min.replace(tzinfo=dt.UTC)
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def pin_cid(token, cid, name):
    return api_request(
        token,
        "POST",
        "/pins",
        body={
            "cid": cid,
            "name": name,
        },
    )


def list_workflow_pins(token):
    pins = []
    after = None

    while True:
        query = {"limit": 100}
        if after:
            query["after"] = after

        payload = api_request(token, "GET", "/pins", query=query)
        results = payload.get("results", [])
        for item in results:
            pin = item.get("pin") or {}
            name = pin.get("name") or ""
            if name.startswith(PIN_NAME_PREFIX):
                pins.append(item)

        if len(results) < query["limit"]:
            break
        after = results[-1].get("created")
        if not after:
            break

    return pins


def find_existing_workflow_pin(pins, cid):
    for item in pins:
        pin = item.get("pin") or {}
        if pin.get("cid") == cid:
            return item
    return None


def delete_pins(token, request_ids):
    for request_id in request_ids:
        api_request(token, "DELETE", f"/pins/{urllib.parse.quote(request_id, safe='')}")
