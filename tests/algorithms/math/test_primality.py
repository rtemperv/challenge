import unittest
from src.algorithms.math.primality import miller_rabin, exhaustive_is_prime
import random


class TestPrimality(unittest.TestCase):

    def test_miller_rabin(self):

        for _ in range(100):
            n = random.randint(1, 100000)
            # assert exhaustive_is_prime(n) == miller_rabin(n)
