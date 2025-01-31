import trimesh

def convert_obj_to_stl(input_path, output_path):
    """Convert OBJ file to STL format."""
    mesh = trimesh.load(input_path)
    mesh.export(output_path)
    print(f"Converted {input_path} to {output_path}")

if __name__ == "__main__":
    input_file = "data/sample_asset.obj"
    output_file = "data/sample_asset.stl"
    convert_obj_to_stl(input_file, output_file)
