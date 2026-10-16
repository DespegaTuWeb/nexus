import urllib.request
import json

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode('utf-8'))

all_media = []
for page in range(1, 5):
    try:
        url = f'https://nexusmotos.com/wp-json/wp/v2/media?per_page=100&page={page}'
        data = fetch_json(url)
        if not data:
            break
        all_media.extend(data)
        print(f"Page {page}: {len(data)} items")
    except Exception as e:
        print(f"Page {page} error or end: {e}")
        break

print(f"Total media found: {len(all_media)}")

# Save all media to json
with open('scripts/all_media.json', 'w', encoding='utf-8') as f:
    json.dump(all_media, f, indent=2, ensure_ascii=False)
print("Saved scripts/all_media.json")
