import unittest

import random
from src.algorithms.sorting import radix_sort


class TestRadixSort(unittest.TestCase):
    def test_sort(self):
        array = [random.randint(1, 100) for _ in range(20)]

        array = radix_sort(array)

        assert array == sorted(array)

    def test_sort_custom_fn(self):
        array = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(20)]

        array = radix_sort(array, lambda x: x[1])

        assert array == sorted(array, key=lambda x: x[1])
