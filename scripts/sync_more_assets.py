import urllib.request
import os

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

more_cutouts = {
    'public/images/bikes/multiproposito-150-delivery.png': 'https://nexusmotos.com/wp-content/uploads/2025/05/MULTIPROPOSITO-150-DELIVERY.png',
    'public/images/bikes/multiproposito-150-ch1.png': 'https://nexusmotos.com/wp-content/uploads/2025/05/MULTIPROPOSITO-150-CH1.png',
    'public/images/bikes/deportiva-250-rsport.png': 'https://nexusmotos.com/wp-content/uploads/2025/05/DEPORTIVA-250-RSPORT.png',
    'public/images/bikes/deportiva-250-rr.png': 'https://nexusmotos.com/wp-content/uploads/2025/05/DEPORTIVA-250-RR.png',
    'public/images/bikes/deportiva-200-rr.png': 'https://nexusmotos.com/wp-content/uploads/2025/05/DEPORTIVA-200-RR.png',
    'public/images/bikes/caferacer-britania-69.png': 'https://nexusmotos.com/wp-content/uploads/2025/05/CAFERACER-BRITANIA-69.png',
    'public/images/bikes/caferacer-200-vx.png': 'https://nexusmotos.com/wp-content/uploads/2025/05/CAFERACER-200-VX.png',
    'public/images/bikes/deportiva-200-ss.png': 'https://nexusmotos.com/wp-content/uploads/2025/05/nexus_WEB-MOTOS_0033_200SS_perfil_negro-amarillo.png',
    # Official banners
    'public/images/banners/banner-carrusel-1.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/web_CARRUSEL-NEXUS-1.png',
    'public/images/banners/banner-carrusel-2.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/web_CARRUSEL-NEXUS-2.png',
    'public/images/banners/banner-carrusel-3.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/web_CARRUSEL-NEXUS-3.png',
}

def main():
    for target, url in more_cutouts.items():
        download_file(url, target)

if __name__ == '__main__':
    main()
