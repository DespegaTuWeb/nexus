import urllib.request
import json
import re
from html import unescape

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

req = urllib.request.Request('https://nexusmotos.com/wp-json/wp/v2/pages?slug=garantia', headers=HEADERS)
with urllib.request.urlopen(req) as resp:
    pages = json.loads(resp.read().decode('utf-8'))

content = pages[0]['content']['rendered']
text = re.sub(r'<[^>]+>', '\n', content)
lines = [unescape(l.strip()) for l in text.splitlines() if l.strip()]

with open('scripts/workshops.txt', 'w', encoding='utf-8') as f:
    for l in lines:
        f.write(l + '\n')

print(f"Saved {len(lines)} lines to scripts/workshops.txt")
