import unittest
import random
from src.topcoder.sorting import quick_sort


class TestQuickSort(unittest.TestCase):
    def test_inplace_sort(self):
        array = [random.randint(1, 100) for _ in range(20)]

        array = quick_sort(array)

        assert array == sorted(array)