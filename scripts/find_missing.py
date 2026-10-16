import json

with open('scripts/all_media.json', encoding='utf-8') as f:
    media = json.load(f)

targets = ['delivery', 'ch1', 'rsport', 'rr', 'britania', 'vx', '200ss']

for m in media:
    url = m.get('source_url', '')
    title = m.get('title', {}).get('rendered', '')
    for t in targets:
        if t in url.lower() or t in title.lower():
            if url.endswith(('.png', '.PNG')):
                print(f"[{t}] {title} -> {url}")
