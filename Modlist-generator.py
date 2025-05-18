import os
import hashlib
import json

# Config
MODS_DIR = "forgemods/required"
REPO_BASE_URL = "https://raw.githubusercontent.com/CreateModFan154/create-the-blueprint-expedition-mods/main/forgemods/required"

# Helpers
def compute_md5(filepath):
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Main
mod_entries = []

if not os.path.exists(MODS_DIR):
    print(f"❌ Directory not found: {MODS_DIR}")
    exit(1)

for filename in os.listdir(MODS_DIR):
    if filename.endswith(".jar"):
        filepath = os.path.join(MODS_DIR, filename)
        filesize = os.path.getsize(filepath)
        md5_hash = compute_md5(filepath)

        entry = {
            "id": f"{filename}:@jar",
            "name": filename,
            "type": "ForgeMod",
            "artifact": {
                "size": filesize,
                "url": f"{REPO_BASE_URL}/{filename}",
                "MD5": md5_hash
            }
        }

        mod_entries.append(entry)

# Output
output_path = "mods_manifest.json"
with open(output_path, "w") as f:
    json.dump(mod_entries, f, indent=2)

print(f"✅ Manifest saved to {output_path}")
