import unittest

from src.algorithms.select.select import quick_select, heap_smallest


class TestSelect(unittest.TestCase):

    def setUp(self):
        self.array = [4, 3, 6, 4, 76, 10]

    def test_quick_select(self):

        assert 4 == quick_select(self.array, 2)
        assert 3 == quick_select(self.array, 0)
        assert 10 == quick_select(self.array, 4)
        assert quick_select(self.array, 6) is None
        assert quick_select([], 0) is None

    def test_heap_select(self):
        assert 4 == heap_smallest(self.array, 2)
        assert 3 == heap_smallest(self.array, 0)
        assert 10 == heap_smallest(self.array, 4)
        assert heap_smallest(self.array, 6) is None
        assert heap_smallest([], 0) is None
