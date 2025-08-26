import json
import os

from flask import current_app, url_for


def load_manifest():
    path = os.path.join(current_app.root_path, current_app.config['STATIC_DIR'], '.vite', 'manifest.json')
    with open(path) as f:
        return json.load(f)

def vite_asset(filename: str):
    if not filename.startswith("src/"):
        filename = f"src/{filename}"

    if current_app.config['ENV'] == 'development':
        return {
            "js": f"{current_app.config['VITE_URL_DEV']}/{filename}",
            "css": [],
            "client": f"{current_app.config['VITE_URL_DEV']}/@vite/client"
        }
    
    manifest = load_manifest()
    entry = manifest.get(filename)

    js_file = url_for('static', filename=f"assets/{entry['file']}")
    css_files = [
        url_for('static', filename=f"assets/{css}") for css in entry.get('css', [])
    ]
    
    return {
        "js": js_file,
        "css": css_files,
        "client": None
    }