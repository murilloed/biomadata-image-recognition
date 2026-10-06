import unittest
from PIL import Image
from biomavision.core import compare

class Tests(unittest.TestCase):
    def test_identical_images(self):
        image = Image.new("L",(64,64),80)
        self.assertEqual(compare(image,image)["changed_cells"],0)

    def test_full_change(self):
        result = compare(Image.new("L",(32,32),0),Image.new("L",(32,32),255))
        self.assertEqual(result["changed_percent"],100)
        self.assertEqual(result["mean_difference"],255)

    def test_threshold_boundary(self):
        a,b = Image.new("L",(32,32),0),Image.new("L",(32,32),30)
        self.assertEqual(compare(a,b,30)["changed_cells"],0)
        self.assertEqual(compare(a,b,29)["changed_cells"],1024)

    def test_invalid_inputs(self):
        a=Image.new("L",(32,32))
        with self.assertRaises(ValueError):
            compare(a,Image.new("L",(64,64)))
        for value in [0,256,float("nan"),float("inf")]:
            with self.assertRaises(ValueError):
                compare(a,a,value)
