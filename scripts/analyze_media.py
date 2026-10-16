import json

with open('scripts/all_media.json', encoding='utf-8') as f:
    media = json.load(f)

print(f"Total media: {len(media)}")

categories = {
    'cutouts': [],
    'photos': [],
    'logos': [],
    'pdfs': [],
    'other': []
}

for m in media:
    url = m.get('source_url', '')
    title = m.get('title', {}).get('rendered', '')
    mime = m.get('mime_type', '')
    
    if 'pdf' in mime:
        categories['pdfs'].append((title, url))
    elif any(k in url.lower() for k in ['logo', 'pictograma', 'marca']):
        categories['logos'].append((title, url))
    elif any(k in url for k in ['TODOTERRENO-', 'MULTIPROPOSITO-', 'SCOOTER-', 'PISTERAS-', 'DEPORTIVAS-', 'Photoroom', 'perfil-derech', 'perfil-izquierd', 'diagonal']):
        categories['cutouts'].append((title, url))
    elif 'image' in mime:
        categories['photos'].append((title, url))
    else:
        categories['other'].append((title, url))

print(f"\nPDFs ({len(categories['pdfs'])}):")
for t, u in categories['pdfs']:
    print(f"  - {t}: {u}")

print(f"\nLogos ({len(categories['logos'])}):")
for t, u in categories['logos']:
    print(f"  - {t}: {u}")

print(f"\nCutouts / Studio Renders ({len(categories['cutouts'])}):")
for t, u in categories['cutouts'][:25]:
    print(f"  - {t}: {u}")
print(f"  ... and {max(0, len(categories['cutouts']) - 25)} more cutouts")
