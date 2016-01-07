import unittest
import random
from src.topcoder.sorting.heapsort import heapsort


class TestHeapSort(unittest.TestCase):

    def test_inplace_sort(self):
        array = [random.randint(1, 100) for _ in range(20)]

        heapsort(array)

        assert array == sorted(array)