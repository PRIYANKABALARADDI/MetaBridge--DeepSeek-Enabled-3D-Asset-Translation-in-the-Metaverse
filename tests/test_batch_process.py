import unittest
import os
from scripts.batch_process import batch_convert

class TestBatchProcessing(unittest.TestCase):
    def test_batch_conversion(self):
        """Test batch conversion of assets."""
        batch_convert("data/")
        for file in os.listdir("data/"):
            if file.endswith(".stl"):
                self.assertTrue(os.path.exists(os.path.join("data/", file)))

if __name__ == "__main__":
    unittest.main()
