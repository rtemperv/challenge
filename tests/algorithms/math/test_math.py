from src.algorithms.math import gcd, lcm
import unittest


class TestMath(unittest.TestCase):

    def test_gcd(self):

        assert gcd(9, 99) == 9

    def test_lcd(self):
        assert lcm(4, 5) == 20
        assert lcm(8, 4) == 8
        assert lcm(124, 77) == 9548
