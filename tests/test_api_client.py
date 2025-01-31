import unittest
from unittest.mock import patch
from scripts.api_client import upload_asset

class TestAPIClient(unittest.TestCase):
    @patch("scripts.api_client.requests.post")
    def test_upload_asset(self, mock_post):
        """Test asset upload API call."""
        mock_post.return_value.json.return_value = {"status": "success"}
        response = upload_asset("data/sample_asset.obj")
        self.assertIsNotNone(response)

if __name__ == "__main__":
    unittest.main()
