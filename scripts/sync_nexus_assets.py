import urllib.request
import json
import os
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def download_file(url, target_path):
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    try:
        print(f"Downloading {url} -> {target_path}")
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp, open(target_path, 'wb') as f:
            f.write(resp.read())
        print(f"  OK: {os.path.getsize(target_path)} bytes")
        return True
    except Exception as e:
        print(f"  Failed: {e}")
        return False

# 1. Download Core Assets & Logos
assets_to_download = {
    'public/images/logo-nexus.png': 'https://nexusmotos.com/wp-content/uploads/2025/04/LOGO-NEXUS_web.png',
    'public/images/nexus-pictograma.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/cropped-NEXUS-pictograma-04-192x192.png',
    'public/images/nexus-mas-peruano.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/LOGO_MAS-PERUANO-NEXUS.png',
    'public/images/nexus-garantia.png': 'https://nexusmotos.com/wp-content/uploads/2025/08/NEXUS_GARANTIA.png',
    'public/images/nexus-anos.png': 'https://nexusmotos.com/wp-content/uploads/2025/08/NEXUS_ANOS.png',
    'public/images/nexus-en-el-peru.png': 'https://nexusmotos.com/wp-content/uploads/2025/08/NEXUS_EN-EL-PERU.png',
}

# 2. Key Model Cutouts
bike_cutouts = {
    'public/images/bikes/todoterreno-250-adv.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/TODOTERRENO-250-ADV.png',
    'public/images/bikes/todoterreno-250-tk.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/TODOTERRENO-250-TK.png',
    'public/images/bikes/todoterreno-250-xr.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/TODOTERRENO-250-XR.png',
    'public/images/bikes/todoterreno-250-xl.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/TODOTERRENO-250-XL.png',
    'public/images/bikes/todoterreno-200-zz.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/TODOTERRENO-200-ZZ.png',
    'public/images/bikes/todoterreno-200-dm.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/TODOTERRENO-200-DM.png',
    'public/images/bikes/multiproposito-200-puma.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/MULTIPROPOSITO-200-PUMA.png',
    'public/images/bikes/multiproposito-200-cb3.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/MULTIPROPOSITO-200-CB3.png',
    'public/images/bikes/multiproposito-150-puma.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/MULTIPROPOSITO-150-PUMA.png',
    'public/images/bikes/multiproposito-150-plusor.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/MULTIPROPOSITO-150-PLUSOR.png',
    'public/images/bikes/150-gl.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/150gl_PERFIL-DERECHO-ROJO-scaled.png',
    'public/images/bikes/multiproposito-150-dk.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/MULTIPROPOSITO-150-DK.png',
    'public/images/bikes/multiproposito-150-delivery.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/MULTIPROPOSITO-150-DELIVERY.png',
    'public/images/bikes/multiproposito-150-ch1.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/MULTIPROPOSITO-150-CH1.png',
    'public/images/bikes/scooter-150-tax.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/SCOOTER-150-TAX.png',
    'public/images/bikes/deportiva-250-rsport.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/DEPORTIVA-250-RSPORT.png',
    'public/images/bikes/deportiva-250-rr.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/DEPORTIVA-250-RR.png',
    'public/images/bikes/caferacer-britania-69.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/CAFERACER-BRITANIA-69.png',
    'public/images/bikes/caferacer-200-vx.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/CAFERACER-200-VX.png',
}

def main():
    print("=== Downloading Logos & Badges ===")
    for target, url in assets_to_download.items():
        download_file(url, target)

    print("\n=== Downloading Official Bike Transparent Cutouts ===")
    for target, url in bike_cutouts.items():
        download_file(url, target)

    print("\nAll downloads completed.")

if __name__ == '__main__':
    main()
