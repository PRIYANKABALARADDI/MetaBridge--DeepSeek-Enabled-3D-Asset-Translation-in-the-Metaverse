import os

def cleanup_directory(directory):
    """Remove temporary files from a given directory."""
    for file in os.listdir(directory):
        if file.endswith(".tmp") or file.endswith(".log"):
            os.remove(os.path.join(directory, file))
            print(f"Deleted {file}")

if __name__ == "__main__":
    cleanup_directory("data/")
