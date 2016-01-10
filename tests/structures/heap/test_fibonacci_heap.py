import unittest
from src.structures import FibonacciHeap
import random


class TestFibonacciHeap(unittest.TestCase):
    def setUp(self):
        self.list = [random.randint(1, 20) for _ in range(10)]
        self.heap = FibonacciHeap(self.list)

        self.list2 = [random.randint(1, 20) for _ in range(10)]
        self.heap2 = FibonacciHeap(self.list2)

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
        heap = FibonacciHeap()

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

    def test_merge(self):

        self.heap.merge(self.heap2)

        assert len(self.heap) == 20

        start = 0
        combined_list = self.list + self.list2
        while True:
            try:
                value = self.heap.pop()
                assert value >= start
                assert value in combined_list
                combined_list.remove(value)
                start = value
            except IndexError:
                break
        assert len(combined_list) == 0
