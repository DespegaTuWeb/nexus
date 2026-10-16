import json

with open('src/data/bikes.json', 'r', encoding='utf-8') as f:
    bikes = json.load(f)

# Sort by price ascending (menor a mayor) as requested by user
bikes.sort(key=lambda b: b.get('rawPricePen', 0))

with open('src/data/bikes.json', 'w', encoding='utf-8') as f:
    json.dump(bikes, f, indent=2, ensure_ascii=False)

print('Bikes successfully ordered by PRICE ASCENDING (Menor a Mayor)!')
for idx, b in enumerate(bikes, 1):
    print(f"{idx}. {b['name']} | {b['categoryLabel']} | {b['cc']} | {b['priceFromPen']}")
