import urllib.request
import json
import re
from html import unescape

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode('utf-8'))

test_slugs = ['250-xr', '200-zz', '150-gl', '150-delivery', '250-tk']

for slug in test_slugs:
    print(f"\n==================== SLUG: {slug} ====================")
    pages = fetch_json(f'https://nexusmotos.com/wp-json/wp/v2/pages?slug={slug}')
    if not pages:
        continue
    p = pages[0]
    content = p['content']['rendered']
    # remove tags
    text = re.sub(r'<[^>]+>', '\n', content)
    lines = [unescape(l.strip()) for l in text.splitlines() if l.strip()]
    print(f"Featured media ID: {p.get('featured_media')}")
    print("Non-empty lines:")
    for l in lines[:30]:
        print("  ", l)
