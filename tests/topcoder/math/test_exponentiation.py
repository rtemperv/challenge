
import unittest
from src.topcoder.math.exponentiation import exponentiation_by_squaring


class TestExponentiation(unittest.TestCase):

    def test_exponentiation(self):

        assert exponentiation_by_squaring(3, 3) == 27

        assert exponentiation_by_squaring(0, 324) == 1

        assert exponentiation_by_squaring(8, 45) == 16815125390625
