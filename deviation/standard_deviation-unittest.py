__author__ = "Shiven"

import unittest
from io import StringIO
from unittest.mock import patch
from standard_deviation import StandardDeviation

class TestStandardDeviation(unittest.TestCase):

    simple_input_1 = iter(["10 40 30 50 20"]).__next__

    @patch("builtins.input", simple_input_1)
    def test_standard_deviation_1(self):
        stndrd_dev = StandardDeviation()
        out = StringIO()
        with patch("sys.stdout", out) as fakeOutput:
            stndrd_dev.cal_deviation()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "14.1")

    simple_input_2 = iter(["10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240 250 260 270 280 290 300"]).__next__

    @patch("builtins.input", simple_input_2)
    def test_weighted_mean_2(self):
        stndrd_dev = StandardDeviation()
        out = StringIO()
        with patch("sys.stdout", out) as fakeOutput:
            stndrd_dev.cal_deviation()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "88.03")

if __name__ == "__main__":
    unittest.main()
