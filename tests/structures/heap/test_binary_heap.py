import unittest
from src.structures import BinaryHeap
import random


class TestBinaryHeap(unittest.TestCase):
    def setUp(self):
        self.list = [random.randint(1, 20) for _ in range(10)]
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

    def test_insert(self):
        heap = BinaryHeap()

        heap.insert(4)
        heap.insert(7)
        heap.insert(1)
        heap.insert(2)
        heap.insert(10)

        assert heap.pop() == 1

        heap.insert(3)

        assert heap.pop() == 2
        assert heap.pop() == 3
        assert heap.pop() == 4
        assert heap.pop() == 7
        assert heap.pop() == 10
