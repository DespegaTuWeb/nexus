import json

with open('src/data/bikes.json', 'r', encoding='utf-8') as f:
    bikes = json.load(f)

deportivas_ids = {
    'nexus-250-rsport',
    'nexus-250-rr',
    'nexus-200-rr',
    'nexus-200-ss'
}

pisteras_ids = {
    'nexus-150-gl',
    'nexus-150-delivery',
    'nexus-150-dk',
    'nexus-150-plusor',
    'nexus-200-cb3',
    'nexus-150-puma',
    'nexus-200-puma'
}

for b in bikes:
    bid = b['id']
    if bid in deportivas_ids:
        b['category'] = 'deportivas'
        b['categoryLabel'] = 'Deportivas'
    elif bid in pisteras_ids:
        b['category'] = 'pisteras'
        b['categoryLabel'] = 'Pisteras'

# Ensure sorted by price ascending
bikes.sort(key=lambda b: b.get('rawPricePen', 0))

with open('src/data/bikes.json', 'w', encoding='utf-8') as f:
    json.dump(bikes, f, indent=2, ensure_ascii=False)

print("Categories reclassified successfully!")
for b in bikes:
    print(f"[{b['category']}] {b['name']} | {b['cc']} | {b['priceFromPen']}")
