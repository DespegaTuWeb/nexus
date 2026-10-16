import json
import re

with open('scripts/all_media.json', encoding='utf-8') as f:
    media = json.load(f)

# Collect all transparent PNG cutouts
cutouts = {}
for m in media:
    url = m.get('source_url', '')
    title = m.get('title', {}).get('rendered', '')
    if not url.endswith(('.png', '.PNG')):
        continue
    
    # Check if it represents a bike
    filename = url.split('/')[-1]
    # Check common patterns
    cutouts[filename] = {
        'title': title,
        'url': url,
        'id': m.get('id')
    }

print(f"Total PNG images in media: {len(cutouts)}")

# Group by bike models
model_images = {}
for fn, data in cutouts.items():
    # Look for model indicators
    lower = fn.lower()
    # Find match
    for pattern in ['250-adv', '250adv', '250-tk', '250tk', '250-xr', '250xr', '250-xl', '250xl', '250-dm', '250dm', '250-rsport', '250rsport', '250-rr', '250rr',
                    '200-zz', '200zz', '200-dm', '200dm', '200-puma', 'puma-200', '200-cb3', '200cb3', '200-xt', '200xt', '200-z', '200z', '200-ss', '200ss', '200-vx', '200vx',
                    '150-puma', 'puma-150', '150-pulsor', '150-plusor', '150-gl', '150gl', '150-dk', '150dk', '150-delivery', '150-ch', '150-tax', 'britania']:
        if pattern in lower:
            base_model = pattern.replace('-', '')
            if base_model not in model_images:
                model_images[base_model] = []
            model_images[base_model].append((fn, data['url']))
            break

print(f"\nRecognized models with PNG cutouts: {len(model_images)}")
for model, imgs in model_images.items():
    print(f"- {model.upper()} ({len(imgs)} PNGs): primary = {imgs[0][0]}")
