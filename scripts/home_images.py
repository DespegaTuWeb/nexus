import urllib.request
import json
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

req = urllib.request.Request('https://nexusmotos.com/wp-json/wp/v2/pages?slug=home', headers=HEADERS)
with urllib.request.urlopen(req) as resp:
    pages = json.loads(resp.read().decode('utf-8'))

p = pages[0]
content = p['content']['rendered']

imgs = re.findall(r'src=["\'](https?://nexusmotos\.com/wp-content/uploads/[^"\']+)["\']', content)
print("Home page images:")
for img in set(imgs):
    print(" ", img)
