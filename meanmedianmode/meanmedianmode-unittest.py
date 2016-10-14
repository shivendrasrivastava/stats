__author__ = "Shiven"

import unittest
from unittest.mock import patch
from meanmedianmode import MeanMedianMode
from io import StringIO

class TestMeanMedianMode(unittest.TestCase):

    sample_input_1 = iter(["64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"]).__next__

    @patch("builtins.input", sample_input_1)
    def test_mean_median_mode_1(self):
        mmm_obj = MeanMedianMode()
        out = StringIO
        with patch("sys.stdout", out) as fakeOutput:
            mmm_obj.calculate_mmm()
        output = fakeOutput.getvalue().strip()
        self.assertEqual(output, "43900.6\n44627.5\n4978")

if __name__ == "__main__":
    unittest.main()
