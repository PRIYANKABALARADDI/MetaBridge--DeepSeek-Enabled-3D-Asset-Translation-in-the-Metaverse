import unittest
import os
from scripts.convert_asset import convert_obj_to_stl

class TestAssetConversion(unittest.TestCase):
    def test_convert_obj_to_stl(self):
        """Test OBJ to STL conversion."""
        input_file = "data/sample_asset.obj"
        output_file = "data/sample_asset.stl"
        convert_obj_to_stl(input_file, output_file)
        self.assertTrue(os.path.exists(output_file))

if __name__ == "__main__":
    unittest.main()
