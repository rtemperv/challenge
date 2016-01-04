from code.structures import Queue
from nose.tools import assert_raises


def test_queue():
    queue = Queue()

    queue.enqueue(5)

    assert len(queue) == 1

    queue.enqueue(2)

    assert len(queue) == 2

    assert queue.dequeue() == 5

    assert queue.dequeue() == 2

    assert queue.is_empty()

    assert_raises(IndexError, queue.dequeue)

