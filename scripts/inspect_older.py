import urllib.request
import json
import re
from html import unescape

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode('utf-8'))

older_slugs = ['250-dm', '200-xt', 'britania-69', '250-rsport', 'nosotros', 'garantia']

for slug in older_slugs:
    print(f"\n==================== {slug} ====================")
    pages = fetch_json(f'https://nexusmotos.com/wp-json/wp/v2/pages?slug={slug}')
    if not pages:
        continue
    content = pages[0]['content']['rendered']
    text = re.sub(r'<[^>]+>', '\n', content)
    lines = [unescape(l.strip()) for l in text.splitlines() if l.strip()]
    for l in lines[:25]:
        print(" ", l)
