from src.algorithms.math import gcd, lcm, nth_fibonacci
import unittest


class TestMath(unittest.TestCase):

    def test_gcd(self):

        assert gcd(9, 99) == 9

    def test_lcd(self):
        assert lcm(4, 5) == 20
        assert lcm(8, 4) == 8
        assert lcm(124, 77) == 9548

    def test_nth_fibonacci(self):

        assert [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] == [nth_fibonacci(i) for i in range(0, 10)]

        assert nth_fibonacci(46) == 2971215073
