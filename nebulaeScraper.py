import os
import re
import requests
from urllib.parse import urljoin

BASE_URL = "https://esahubble.org"
TARGET_URL = "https://esahubble.org/images/archive/category/nebulae/page/3/"
DOWNLOAD_DIR = "nebulae_dataset"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def scrape_hubble_nebulae():
    print(f"Connecting to {TARGET_URL}...")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    response = requests.get(TARGET_URL, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return

    raw_html = response.text
    img_paths = set(re.findall(r'(/archives/images/[^"\'>]+\.jpg|https?://cdn\.[a-zA-Z0-9\.-]+/archives/images/[^"\'>]+\.jpg)', raw_html))
    
    if not img_paths:
        print("No image URLs found.")
        img_paths = set(re.findall(r'(https?://[^"\'>\s]+\.jpg)', raw_html))

    downloaded_count = 0
    
    for path in img_paths:
        if path.startswith("http"):
            img_url = path
        else:
            img_url = urljoin(BASE_URL, path)
            
            
        if "thumb300y" in img_url:
            img_url = img_url.replace("thumb300y", "screen")
        if "logo" in img_url.lower() or "icon" in img_url.lower():
            continue

        filename = img_url.split("/")[-1]
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        
        try:
            img_data = requests.get(img_url, headers=headers, timeout=10).content
            if len(img_data) > 5000: 
                with open(filepath, "wb") as handler:
                    handler.write(img_data)
                
                print(f"[{downloaded_count+1}] Downloaded: {filename}")
                downloaded_count += 1
                if downloaded_count >= 150:
                    break
            else:
                print(f"Skipped {filename} (File too small, likely a placeholder)")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")
            
            
    print(f"\nDownloaded {downloaded_count} Nebula images to '{DOWNLOAD_DIR}'.")

if __name__ == "__main__":
    scrape_hubble_nebulae()