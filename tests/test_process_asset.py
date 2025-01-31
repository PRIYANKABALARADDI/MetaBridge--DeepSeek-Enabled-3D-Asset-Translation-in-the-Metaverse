import unittest
from scripts.process_asset import analyze_asset

class TestAssetProcessing(unittest.TestCase):
    def test_analyze_asset(self):
        """Test the asset metadata extraction."""
        file_path = "data/sample_asset.obj"
        metadata = analyze_asset(file_path)
        self.assertIsInstance(metadata, dict)
        self.assertIn("vertices", metadata)
        self.assertIn("faces", metadata)

if __name__ == "__main__":
    unittest.main()
