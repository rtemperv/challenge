
from src.algorithms.dynamic.longest_chain_in_matrix import find_longest_chain_in_matrix
import unittest


class TestLongestChainInMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = [
            [1, 2, 3, 4],
            [1, 2, 3, 5],
            [1, 2, 7, 6],
            [1, 2, 3, 4],
        ]

        self.matrix2 = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]

    def test_longest_chain_in_matrix(self):
        assert find_longest_chain_in_matrix(self.matrix, 4) == 7

        assert find_longest_chain_in_matrix(self.matrix2, 5) == 1
