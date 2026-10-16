import urllib.request
import json

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode('utf-8'))

def main():
    # Let's fetch media items
    print("Fetching media items...")
    media = fetch_json('https://nexusmotos.com/wp-json/wp/v2/media?per_page=100')
    print(f"Total media items in page 1: {len(media)}")
    for m in media:
        title = m['title']['rendered']
        src = m['source_url']
        mime = m['mime_type']
        if 'image' in mime:
            print(f"- [IMG] {title} -> {src}")
        elif 'pdf' in mime:
            print(f"- [PDF] {title} -> {src}")

if __name__ == '__main__':
    main()
