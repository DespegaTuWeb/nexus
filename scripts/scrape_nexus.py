import urllib.request
import json
import os
from html import unescape

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode('utf-8'))

def main():
    pages_url = 'https://nexusmotos.com/wp-json/wp/v2/pages?per_page=100'
    print("Fetching pages from nexusmotos.com...")
    pages = fetch_json(pages_url)
    print(f"Total pages: {len(pages)}")

    for p in pages:
        title = unescape(p['title']['rendered'])
        slug = p['slug']
        media_id = p.get('featured_media')
        print(f"[{p['id']}] {slug} -> '{title}' (media: {media_id})")

if __name__ == '__main__':
    main()
