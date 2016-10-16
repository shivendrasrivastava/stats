__author__ = "Shiven"

import unittest
from io import StringIO
from unittest.mock import patch
from weighted_mean import cal_wghtd_mean

class TestWeightedMean(unittest.TestCase):

    simple_input_1 = iter(["10 40 30 50 20", "1 2 3 4 5"]).__next__

    @patch("builtins.input", simple_input_1)
    def test_weighted_mean_1(self):
        out = StringIO()
        with patch("sys.stdout", out) as fakeOutput:
            cal_wghtd_mean()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "32.0")

    simple_input_2 = iter(["10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200", "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"]).__next__

    @patch("builtins.input", simple_input_2)
    def test_weighted_mean_2(self):
        out = StringIO()
        with patch("sys.stdout", out) as fakeOutput:
            cal_wghtd_mean()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "136.6667")

if __name__ == "__main__":
    unittest.main()
