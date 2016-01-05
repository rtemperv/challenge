from src.structures import Queue
from nose.tools import assert_raises
import unittest


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.empty_queue = Queue()

    def test_dequeue(self):
        assert self.queue.dequeue() == 1
        assert self.queue.dequeue() == 2
        assert self.queue.dequeue() == 3
        assert_raises(IndexError, self.queue.dequeue)

    def test_enqueue(self):
        self.queue.enqueue(7)
        assert len(self.queue) == 4

    def test_is_empty(self):
        assert self.empty_queue.is_empty()

    def test_peek(self):
        assert self.queue.peek() == self.queue.peek()
        assert self.queue.peek() == 1
        assert len(self.queue) == 3
        assert_raises(IndexError, self.empty_queue.peek)
