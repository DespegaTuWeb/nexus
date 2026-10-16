import urllib.request
import json
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode('utf-8'))

# Check scooter category page
try:
    p = fetch_json('https://nexusmotos.com/wp-json/wp/v2/pages?slug=scooter')[0]
    content = p['content']['rendered']
    links = re.findall(r'href=["\'](https?://nexusmotos\.com/[^"\']+)["\']', content)
    print("Links in scooter page:")
    for l in set(links):
        print(" ", l)
except Exception as e:
    print("Error:", e)

# Also check scooter slugs
scooter_slugs = ['150-tax', '150-t4', '150-t3', '150-t', '150-ts', '125-tx', '150-tx']
for s in scooter_slugs:
    try:
        pages = fetch_json(f'https://nexusmotos.com/wp-json/wp/v2/pages?slug={s}')
        if pages:
            title = pages[0]['title']['rendered']
            print(f"Model [{s}]: {title}")
    except Exception as e:
        print(f"Error {s}: {e}")
