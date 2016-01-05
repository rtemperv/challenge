import unittest
from src.structures import BinaryHeap
import random


class TestBinaryHeap(unittest.TestCase):
    def setUp(self):
        self.list = [random.randint(1,20) for _ in range(10)]
        self.heap = BinaryHeap(self.list)

    def test_pop(self):
        start = 0
        while True:
            try:
                value = self.heap.pop()
                assert value >= start
                assert value in self.list
                self.list.remove(value)
                start = value
            except IndexError:
                break
        assert len(self.list) == 0
