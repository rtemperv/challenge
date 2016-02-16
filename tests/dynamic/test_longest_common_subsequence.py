import unittest
from src.algorithms.dynamic.longest_increasing_subsequence import longest_increasing_subsequence


class TestLongestCommonSubsequence(unittest.TestCase):
    def test_1(self):
        assert longest_increasing_subsequence([1, 7, 2, 1, 3, 3, 4]) == [1, 2, 3, 4]

    def test_1(self):
        assert longest_increasing_subsequence(list(range(10))) == list(range(10))
