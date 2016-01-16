from src.algorithms.math import from_base_to_decimal, from_decimal_to_base
import unittest


class TestBases(unittest.TestCase):

    def test_bases(self):

        assert "12F4C9" == from_decimal_to_base(1242313, 16)
        assert 4095 == from_base_to_decimal("FFF", 16)

        assert "13011" == from_decimal_to_base(5641, 8)
