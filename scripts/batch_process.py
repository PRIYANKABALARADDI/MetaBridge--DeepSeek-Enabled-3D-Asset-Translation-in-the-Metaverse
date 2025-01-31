import os
from convert_asset import convert_obj_to_stl

def batch_convert(directory):
    """Convert all OBJ files in a directory to STL format."""
    for file in os.listdir(directory):
        if file.endswith(".obj"):
            input_path = os.path.join(directory, file)
            output_path = input_path.replace(".obj", ".stl")
            convert_obj_to_stl(input_path, output_path)

if __name__ == "__main__":
    batch_convert("data/")
