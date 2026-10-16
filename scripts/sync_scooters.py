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

scooter_cutouts = {
    'public/images/bikes/scooter-150-tax.png': 'https://nexusmotos.com/wp-content/uploads/2025/09/SCOOTER-150-TAX.png',
    'public/images/bikes/scooter-150-t4.png': 'https://nexusmotos.com/wp-content/uploads/2025/05/SCOOTER-150-T4.png',
    'public/images/bikes/scooter-150-t3.png': 'https://nexusmotos.com/wp-content/uploads/2025/05/SCOOTER-150-T3.png',
    'public/images/bikes/scooter-150-t.png': 'https://nexusmotos.com/wp-content/uploads/2025/05/SCOOTER-150-T.png',
    'public/images/bikes/scooter-150-t5.png': 'https://nexusmotos.com/wp-content/uploads/2025/05/SCOOTER-150-T5.png',
    'public/images/bikes/scooter-150-tx.png': 'https://nexusmotos.com/wp-content/uploads/2025/05/SCOOTER-150-TX.png',
    'public/images/bikes/scooter-125-tx.png': 'https://nexusmotos.com/wp-content/uploads/2025/05/SCOOTER-125-TX.png',
}

def main():
    for target, url in scooter_cutouts.items():
        download_file(url, target)

if __name__ == '__main__':
    main()
