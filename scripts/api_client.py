import requests

BASE_URL = "http://localhost:5000"

def upload_asset(file_path):
    """Upload a 3D asset to the API."""
    files = {'file': open(file_path, 'rb')}
    response = requests.post(f"{BASE_URL}/upload", files=files)
    print(response.json())

if __name__ == "__main__":
    upload_asset("data/sample_asset.obj")
