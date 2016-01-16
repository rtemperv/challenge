import unittest
from src.topcoder.dynamic.coins import minimal_coins_iterative


class TestCoins(unittest.TestCase):

    def test_coins(self):

        assert minimal_coins_iterative([1, 2, 5], 77) == 16
        assert minimal_coins_iterative([1, 3, 5], 9) == 3
