import trimesh
import json

def analyze_asset(file_path):
    """Load and extract metadata from a 3D asset file."""
    mesh = trimesh.load(file_path)
    asset_data = {
        "vertices": len(mesh.vertices),
        "faces": len(mesh.faces),
        "texture": None,  # Placeholder for texture data
        "animations": mesh.animation if hasattr(mesh, 'animation') else None
    }
    return asset_data

if __name__ == "__main__":
    file_path = "data/sample_asset.obj"
    metadata = analyze_asset(file_path)
    with open("data/asset_metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)
    print("Asset metadata saved successfully.")
