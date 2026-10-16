import json

with open('scripts/all_media.json', encoding='utf-8') as f:
    media = json.load(f)

for m in media:
    url = m.get('source_url', '')
    if any(k in url.lower() for k in ['logo', 'nexus', 'icon', 'banner', 'lauzher', 'ronco']):
        print(f"[{m['id']}] {m.get('title',{}).get('rendered')} -> {url}")
