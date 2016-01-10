import unittest

import random
from src.algorithms.sorting import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_sort(self):
        array = [random.randint(1, 100) for _ in range(20)]

        array = merge_sort(array)

        assert array == sorted(array)
