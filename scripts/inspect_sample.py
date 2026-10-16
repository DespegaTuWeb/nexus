import json
import re

with open('scripts/sample_page.json', encoding='utf-8') as f:
    text = f.read()

links = re.findall(r'href=["\'](https?://[^"\']+)["\']', text)
print("Found links:")
for l in set(links):
    print(" ", l)
