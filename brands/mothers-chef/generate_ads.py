#!/usr/bin/env python3
"""
Local Service Business Ad Generator
Yerena Digital — Nano Banana 2 via FAL API

Usage:
  python generate_ads.py                          # Run all templates
  python generate_ads.py --templates 1,3,7        # Run specific templates
  python generate_ads.py --templates 1,2,3 --resolution 1K  # Test run
"""

import os
import sys
import json
import time
import argparse
import requests
from pathlib import Path
from datetime import datetime

# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────

FAL_KEY = os.environ.get("FAL_KEY")
if not FAL_KEY:
    print("ERROR: FAL_KEY environment variable not set.")
    print("Run: export FAL_KEY='your-key-here'")
    sys.exit(1)

FAL_BASE = "https://fal.run"
FAL_QUEUE = "https://queue.fal.run"  # backup — currently has stale lock
FAL_UPLOAD = "https://storage.fal.run"
HEADERS = {
    "Authorization": f"Key {FAL_KEY}",
    "Content-Type": "application/json"
}

NUM_IMAGES = 4
DEFAULT_RESOLUTION = "2K"
POLL_INTERVAL = 3
MAX_WAIT = 120

SCRIPT_DIR = Path(__file__).parent
PROMPTS_FILE = SCRIPT_DIR / "prompts.json"
ASSETS_DIR = SCRIPT_DIR / "assets"
OUTPUTS_DIR = SCRIPT_DIR / "outputs"

# ─────────────────────────────────────────────
# FAL STORAGE UPLOAD
# ─────────────────────────────────────────────

def upload_image_to_fal(image_path: Path):
    try:
        with open(image_path, "rb") as f:
            file_data = f.read()
        ext = image_path.suffix.lower()
        mime_types = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}
        mime = mime_types.get(ext, "image/jpeg")
        resp = requests.post(
            FAL_UPLOAD,
            headers={"Authorization": f"Key {FAL_KEY}", "Content-Type": mime},
            data=file_data,
            timeout=30
        )
        if resp.status_code == 200:
            url = resp.json().get("url")
            print(f"  ✓ Uploaded: {image_path.name} → {url[:60]}...")
            return url
        else:
            print(f"  ✗ Upload failed for {image_path.name}: {resp.status_code}")
            return None
    except Exception as e:
        print(f"  ✗ Upload error for {image_path.name}: {e}")
        return None

def get_asset_urls(asset_type: str, reference_urls: list = None) -> list:
    # If public URLs are provided in prompts.json, use those directly (no upload needed)
    if reference_urls:
        print(f"  Using {len(reference_urls)} public reference URL(s) from prompts.json")
        return reference_urls

    # Otherwise try to upload local files
    type_to_folder = {
        "owner": "owner",
        "before_after": "before-after",
        "finished_work": "finished-work",
        "team": "team",
        "review_screenshot": "review-screenshot",
    }
    folder_name = type_to_folder.get(asset_type, asset_type.replace("_", "-"))
    asset_folder = ASSETS_DIR / folder_name
    if not asset_folder.exists():
        asset_folder = ASSETS_DIR
    if not asset_folder.exists():
        print(f"  ⚠ No assets folder found at {asset_folder}")
        return []
    image_extensions = {".jpg", ".jpeg", ".png", ".webp"}
    image_files = [f for f in asset_folder.iterdir() if f.is_file() and f.suffix.lower() in image_extensions]
    if not image_files:
        print(f"  ⚠ No images found in {asset_folder}")
        return []
    urls = []
    for img_path in image_files[:3]:
        url = upload_image_to_fal(img_path)
        if url:
            urls.append(url)
    return urls

# ─────────────────────────────────────────────
# FAL API CALLS
# ─────────────────────────────────────────────

def submit_text_to_image(prompt: str, aspect_ratio: str, resolution: str, num_images: int = NUM_IMAGES):
    payload = {
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "num_images": num_images,
        "output_format": "png",
        "resolution": resolution,
    }
    for attempt in range(3):
        try:
            resp = requests.post(f"{FAL_BASE}/fal-ai/nano-banana-2", headers=HEADERS, json=payload, timeout=120)
            if resp.status_code in (200, 201):
                return resp.json()  # sync endpoint returns full result
            elif resp.status_code == 403:
                print(f"  ✗ Account locked (balance exhausted). Top up at fal.ai/dashboard/billing")
                return "BALANCE_EXHAUSTED"
            else:
                print(f"  ✗ Submit failed: {resp.status_code} {resp.text}")
                return None
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            if attempt < 2:
                print(f"  ⚠ Connection error, retrying ({attempt+1}/3)...")
                time.sleep(3)
            else:
                print(f"  ✗ Submit failed after 3 attempts: {e.__class__.__name__}")
                return None

def submit_image_edit(prompt: str, image_urls: list, aspect_ratio: str, resolution: str, num_images: int = NUM_IMAGES):
    payload = {
        "prompt": prompt,
        "image_urls": image_urls,
        "aspect_ratio": aspect_ratio,
        "num_images": num_images,
        "output_format": "png",
        "resolution": resolution,
    }
    for attempt in range(3):
        try:
            resp = requests.post(f"{FAL_BASE}/fal-ai/nano-banana-2/edit", headers=HEADERS, json=payload, timeout=120)
            if resp.status_code in (200, 201):
                return resp.json()  # sync endpoint returns full result
            elif resp.status_code == 403:
                print(f"  ✗ Account locked (balance exhausted). Top up at fal.ai/dashboard/billing")
                return "BALANCE_EXHAUSTED"
            else:
                print(f"  ✗ Submit failed: {resp.status_code} {resp.text}")
                return None
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            if attempt < 2:
                print(f"  ⚠ Connection error, retrying ({attempt+1}/3)...")
                time.sleep(3)
            else:
                print(f"  ✗ Submit failed after 3 attempts: {e.__class__.__name__}")
                return None

def poll_for_result(request_id: str):
    start = time.time()
    while time.time() - start < MAX_WAIT:
        try:
            resp = requests.get(f"{FAL_BASE}/fal-ai/nano-banana-2/requests/{request_id}/status", headers=HEADERS, timeout=30)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            print(f"  ⚠ Poll connection error, retrying... ({e.__class__.__name__})")
            time.sleep(POLL_INTERVAL * 2)
            continue
        if resp.status_code == 200:
            status_data = resp.json()
            status = status_data.get("status")
            if status == "COMPLETED":
                try:
                    result_resp = requests.get(f"{FAL_BASE}/fal-ai/nano-banana-2/requests/{request_id}", headers=HEADERS, timeout=30)
                    if result_resp.status_code == 200:
                        return result_resp.json()
                except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
                    print(f"  ⚠ Result fetch timed out, retrying...")
                    time.sleep(POLL_INTERVAL)
                    continue
                return None
            elif status == "FAILED":
                print(f"  ✗ Job failed: {status_data.get('error', 'Unknown error')}")
                return None
            else:
                print(f"  ⏳ Status: {status}...", end="\r")
                time.sleep(POLL_INTERVAL)
        elif resp.status_code == 403:
            print(f"  ✗ Account locked (balance exhausted)")
            return None
        else:
            time.sleep(POLL_INTERVAL)
    print(f"  ✗ Timeout after {MAX_WAIT}s")
    return None

# ─────────────────────────────────────────────
# IMAGE DOWNLOAD
# ─────────────────────────────────────────────

def download_images(result: dict, output_dir: Path, template_name: str) -> list:
    images = result.get("images", [])
    saved = []
    for i, img_data in enumerate(images):
        url = img_data.get("url")
        if not url:
            continue
        filename = f"{template_name}_v{i+1}.png"
        dest = output_dir / filename
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            with open(dest, "wb") as f:
                f.write(r.content)
            saved.append(dest)
            print(f"  ✓ Saved: {filename}")
        except Exception as e:
            print(f"  ✗ Download failed for {filename}: {e}")
    return saved

# ─────────────────────────────────────────────
# HTML GALLERY
# ─────────────────────────────────────────────

def generate_gallery(business_name: str, prompts: list, outputs_dir: Path):
    cards = []
    for prompt_data in prompts:
        t_num = prompt_data["template_number"]
        t_name = prompt_data["template_name"]
        folder = outputs_dir / f"{t_num:02d}-{t_name}"
        if not folder.exists():
            continue
        images = sorted(folder.glob("*.png"))
        if not images:
            continue
        img_tags = ""
        for img in images:
            rel_path = img.relative_to(outputs_dir.parent)
            img_tags += f'<img src="{rel_path}" alt="{t_name}" loading="lazy">'
        copy_data = prompt_data.get("copy", {})
        headline = copy_data.get("headline", "")
        cta = copy_data.get("cta", "")
        cards.append(f"""
        <div class="template-card">
            <div class="template-header">
                <span class="template-number">#{t_num:02d}</span>
                <h3>{t_name.replace("-", " ").title()}</h3>
                <span class="aspect">{prompt_data.get("aspect_ratio", "")}</span>
            </div>
            <div class="copy-preview">
                {f'<p class="headline">"{headline}"</p>' if headline else ""}
                {f'<p class="cta">{cta}</p>' if cta else ""}
            </div>
            <div class="image-grid">{img_tags}</div>
        </div>""")

    timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    total_images = sum(
        len(list((outputs_dir / f"{p['template_number']:02d}-{p['template_name']}").glob("*.png")))
        for p in prompts
        if (outputs_dir / f"{p['template_number']:02d}-{p['template_name']}").exists()
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{business_name} — Ad Creative Gallery | Yerena Digital</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Helvetica Neue', Arial, sans-serif; background: #0f0f0f; color: #fff; }}
  header {{ background: #111; border-bottom: 1px solid #222; padding: 24px 32px; display: flex; justify-content: space-between; align-items: center; }}
  header h1 {{ font-size: 20px; font-weight: 700; letter-spacing: -0.5px; }}
  header p {{ font-size: 13px; color: #666; margin-top: 4px; }}
  .badge {{ background: #1a1a1a; border: 1px solid #333; border-radius: 20px; padding: 6px 14px; font-size: 12px; color: #aaa; }}
  .gallery {{ max-width: 1400px; margin: 0 auto; padding: 32px; }}
  .template-card {{ background: #161616; border: 1px solid #222; border-radius: 12px; overflow: hidden; margin-bottom: 40px; }}
  .template-header {{ display: flex; align-items: center; gap: 12px; padding: 16px 20px; background: #1a1a1a; border-bottom: 1px solid #222; }}
  .template-number {{ background: #FF6B35; color: #fff; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 4px; }}
  .template-header h3 {{ font-size: 15px; font-weight: 600; flex: 1; }}
  .aspect {{ font-size: 11px; color: #555; background: #222; padding: 3px 8px; border-radius: 4px; }}
  .copy-preview {{ padding: 12px 20px; background: #131313; border-bottom: 1px solid #1e1e1e; }}
  .copy-preview .headline {{ font-size: 14px; font-style: italic; color: #ccc; }}
  .copy-preview .cta {{ font-size: 12px; color: #666; margin-top: 4px; }}
  .image-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); }}
  .image-grid img {{ width: 100%; display: block; object-fit: cover; cursor: pointer; transition: opacity 0.2s; }}
  .image-grid img:hover {{ opacity: 0.85; }}
  footer {{ text-align: center; padding: 40px; color: #444; font-size: 12px; border-top: 1px solid #1a1a1a; }}
  @media (max-width: 900px) {{ .image-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
</style>
</head>
<body>
<header>
  <div>
    <h1>{business_name} — Static Ad Creative Gallery</h1>
    <p>Generated by Yerena Digital · {timestamp}</p>
  </div>
  <div class="badge">{total_images} images · {len(cards)} templates</div>
</header>
<div class="gallery">{"".join(cards)}</div>
<footer>Generated by Yerena Digital Ad Generator · Powered by Nano Banana 2 via FAL API</footer>
</body>
</html>"""

    gallery_path = SCRIPT_DIR / "index.html"
    with open(gallery_path, "w") as f:
        f.write(html)
    print(f"\n✓ Gallery saved: {gallery_path}")
    return gallery_path

# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Yerena Digital — Local Service Ad Generator")
    parser.add_argument("--templates", type=str, help="Comma-separated template numbers (e.g. 1,3,7)")
    parser.add_argument("--resolution", type=str, default=DEFAULT_RESOLUTION, help="1K | 2K | 4K")
    parser.add_argument("--num-images", type=int, default=NUM_IMAGES, help="Number of images per template (default: 4)")
    parser.add_argument("--prompts-file", type=str, default=None, help="Path to prompts JSON file (default: prompts.json)")
    args = parser.parse_args()

    num_images = args.num_images

    prompts_file = Path(args.prompts_file) if args.prompts_file else PROMPTS_FILE
    if not prompts_file.exists():
        print(f"ERROR: prompts file not found at {prompts_file}")
        sys.exit(1)

    with open(prompts_file) as f:
        data = json.load(f)

    business_name = data.get("business", "Business")
    all_prompts = data.get("prompts", [])

    if args.templates:
        requested = set(int(t.strip()) for t in args.templates.split(","))
        prompts_to_run = [p for p in all_prompts if p["template_number"] in requested]
    else:
        prompts_to_run = all_prompts

    resolution = args.resolution.upper()
    total = len(prompts_to_run)
    cost_per_image = {"1K": 0.08, "2K": 0.12, "4K": 0.16}.get(resolution, 0.12)
    est_cost = total * num_images * cost_per_image

    print(f"\n{'='*60}")
    print(f"  Yerena Digital — Local Service Ad Generator")
    print(f"  Business: {business_name}")
    print(f"  Templates: {total} | Resolution: {resolution} | Images/prompt: {num_images}")
    print(f"  Estimated cost: ~${est_cost:.2f}")
    print(f"{'='*60}\n")

    OUTPUTS_DIR.mkdir(exist_ok=True)
    generated_count = 0

    for i, prompt_data in enumerate(prompts_to_run):
        t_num = prompt_data["template_number"]
        t_name = prompt_data["template_name"]
        prompt_text = prompt_data["prompt"]
        aspect_ratio = prompt_data.get("aspect_ratio", "4:5")
        needs_refs = prompt_data.get("needs_reference_images", False)
        asset_type = prompt_data.get("reference_asset_type", "finished_work")

        print(f"[{i+1}/{total}] Template #{t_num:02d}: {t_name.replace('-', ' ').title()}")

        output_dir = OUTPUTS_DIR / f"{t_num:02d}-{t_name}"
        output_dir.mkdir(exist_ok=True)

        with open(output_dir / "prompt.txt", "w") as f:
            f.write(f"Template: {t_name}\nAspect Ratio: {aspect_ratio}\nResolution: {resolution}\nGenerated: {datetime.now().isoformat()}\n\n{prompt_text}")

        request_id = None

        result = None
        if needs_refs:
            ref_urls = prompt_data.get("reference_urls", None)
            print(f"  Loading reference images (type: {asset_type})...")
            image_urls = get_asset_urls(asset_type, ref_urls)
            if image_urls:
                print(f"  Submitting to /edit endpoint with {len(image_urls)} reference image(s)...")
                result = submit_image_edit(prompt_text, image_urls, aspect_ratio, resolution, num_images)
            else:
                print(f"  ⚠ No reference images found — falling back to text-to-image")
                result = submit_text_to_image(prompt_text, aspect_ratio, resolution, num_images)
        else:
            print(f"  Submitting to text-to-image endpoint...")
            result = submit_text_to_image(prompt_text, aspect_ratio, resolution, num_images)

        if result == "BALANCE_EXHAUSTED":
            print(f"\n  ⛔ Balance exhausted — stopping. Top up at fal.ai/dashboard/billing")
            print(f"  Resume with: --templates {','.join(str(p['template_number']) for p in prompts_to_run[i:])}\n")
            break

        if not result:
            print(f"  ✗ Skipping template #{t_num} — submission failed\n")
            continue

        if isinstance(result, dict) and "images" in result:
            saved = download_images(result, output_dir, t_name)
            generated_count += len(saved)
            print(f"  ✓ {len(saved)} images saved to outputs/{t_num:02d}-{t_name}/\n")
        else:
            print(f"  ✗ Unexpected result for template #{t_num}\n")

        if i < total - 1:
            time.sleep(1)

    print("\nGenerating gallery...")
    gallery_path = generate_gallery(business_name, prompts_to_run, OUTPUTS_DIR)

    print(f"\n{'='*60}")
    print(f"  ✓ Complete! {generated_count} images across {total} templates")
    print(f"  Gallery: {gallery_path}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
