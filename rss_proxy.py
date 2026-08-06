#!/usr/bin/env python3
"""
rss_proxy.py — minimal RSS/Atom proxy + static file server.
- GET /                  -> serves /opt/data/dashboard-prototype/index.html (default file)
- GET /<path>            -> serves file from /opt/data/dashboard-prototype
- GET /api/feed?url=...  -> fetches & parses RSS/Atom, returns JSON list of items
                              [{title, link, src, srcLabel, ts}]
- Caches upstream responses in-memory for CACHE_TTL seconds.
"""

import http.server
import json
import os
import re
import socketserver
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

ROOT = "/opt/data/dashboard-prototype"
PORT = int(os.environ.get("PORT", "8765"))
CACHE_TTL = 300  # 5 minutes
USER_AGENT = "DashboardPrototype/0.1 (+https://trycloudflare.com)"

CACHE = {}  # url -> (fetched_at, items)
HKO_CACHE = {}  # dataType -> (fetched_at, payload)
HKO_TTL = 300  # 5 minutes

ATOM = "{http://www.w3.org/2005/Atom}"
DC = "{http://purl.org/dc/elements/1.1/}"
CONTENT = "{http://purl.org/rss/1.0/modules/content/}"


def _text(node, tag):
    el = node.find(tag)
    return (el.text or "").strip() if el is not None and el.text else ""


def parse_feed(xml_bytes, source_url):
    """Parse RSS 2.0 or Atom feed into a list of dicts."""
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return []
    items = []
    # Detect feed type
    if root.tag == "rss" or root.tag.endswith("}rss"):
        channel_title = _text(root, "channel/title")
        for item in root.findall("./channel/item"):
            title = _text(item, "title")
            link = _text(item, "link")
            pub = _text(item, "pubDate") or _text(item, DC + "date")
            if not title:
                continue
            items.append({
                "title": title,
                "link": link,
                "src": channel_title or "RSS",
                "srcLabel": channel_title or "RSS",
                "ts": format_ts(pub),
            })
    elif root.tag == ATOM + "feed":
        feed_title = _text(root, ATOM + "title")
        for entry in root.findall(ATOM + "entry"):
            title = _text(entry, ATOM + "title")
            link_el = entry.find(ATOM + "link")
            link = link_el.get("href", "") if link_el is not None else ""
            pub = _text(entry, ATOM + "published") or _text(entry, ATOM + "updated")
            if not title:
                continue
            items.append({
                "title": title,
                "link": link,
                "src": feed_title or "Atom",
                "srcLabel": feed_title or "Atom",
                "ts": format_ts(pub),
            })
    return items


def format_ts(raw):
    """Format a date string to relative time (e.g. '10 分鐘前') or YYYY-MM-DD."""
    if not raw:
        return ""
    raw = raw.strip()
    # Try RFC 2822 (RSS)
    try:
        dt = parsedate_to_datetime(raw)
        return rel_time(dt.timestamp())
    except Exception:
        pass
    # Try ISO 8601 (Atom)
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        return rel_time(dt.timestamp())
    except Exception:
        pass
    # Fallback: return first 16 chars
    return raw[:16]


def rel_time(ts):
    """Return relative time string in zh-Hant."""
    from datetime import datetime, timezone
    now = time.time()
    diff = int(now - ts)
    if diff < 60:
        return f"{diff} 秒前"
    if diff < 3600:
        return f"{diff // 60} 分鐘前"
    if diff < 86400:
        return f"{diff // 3600} 小時前"
    if diff < 86400 * 7:
        return f"{diff // 86400} 日前"
    return time.strftime("%Y-%m-%d", time.gmtime(ts))


def fetch_feed(url):
    """Fetch and parse a feed, with cache."""
    now = time.time()
    if url in CACHE:
        fetched_at, items = CACHE[url]
        if now - fetched_at < CACHE_TTL:
            return items
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/rss+xml, application/atom+xml, application/xml;q=0.9, */*;q=0.8",
        })
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = resp.read()
        items = parse_feed(data, url)
        CACHE[url] = (now, items)
        return items
    except Exception as e:
        print(f"[feed error] {url}: {e}", file=sys.stderr)
        return None


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        # Prevent caching so dashboard updates are immediately visible after reload
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):
        # quieter logging
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def do_GET(self):
        if self.path.startswith("/api/feed"):
            self.handle_feed()
        elif self.path.startswith("/api/hko"):
            self.handle_hko()
        else:
            super().do_GET()

    def handle_hko(self):
        qs = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(qs)
        dataType = (params.get("dataType") or ["rhrread"])[0]
        lang = (params.get("lang") or ["tc"])[0]
        cache_key = f"{dataType}|{lang}"
        now = time.time()
        if cache_key in HKO_CACHE and now - HKO_CACHE[cache_key][0] < HKO_TTL:
            self.send_json(200, HKO_CACHE[cache_key][1])
            return
        url = f"https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType={dataType}&lang={lang}"
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": USER_AGENT,
                "Accept": "application/json",
            })
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            HKO_CACHE[cache_key] = (now, data)
            self.send_json(200, data)
        except Exception as e:
            print(f"[hko error] {url}: {e}", file=sys.stderr)
            self.send_json(502, {"error": "hko fetch failed", "detail": str(e)})

    def handle_feed(self):
        qs = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(qs)
        url = (params.get("url") or [None])[0]
        if not url:
            self.send_json(400, {"error": "missing url"})
            return
        items = fetch_feed(url)
        if items is None:
            self.send_json(502, {"error": "fetch failed", "url": url})
            return
        self.send_json(200, {"url": url, "count": len(items), "items": items})

    def send_json(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)


class ReusableTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    print(f"serving {ROOT} on port {PORT} (RSS proxy enabled)", flush=True)
    with ReusableTCPServer(("", PORT), Handler) as srv:
        srv.serve_forever()
