import unittest
import random
from src.topcoder.sorting import heap_sort


class TestHeapSort(unittest.TestCase):

    def test_inplace_sort(self):
        array = [random.randint(1, 100) for _ in range(20)]

        heap_sort(array)

        assert array == sorted(array)