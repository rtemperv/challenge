import unittest

import random
from src.algorithms.sorting import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test_sort(self):
        array = [random.randint(1, 100) for _ in range(20)]

        insertion_sort(array)

        assert array == sorted(array)
