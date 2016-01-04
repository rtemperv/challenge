from .linked_list import LinkedList
from threading import Lock


class Queue(object):
    """
    FIFO queue based on single linked list
    All operations are O(1)
    """
    def __init__(self):
        # Use composition to hide the linked list implementation details
        self._linked_list = LinkedList()
        self._lock = Lock()

    def __len__(self):
        with self._lock:
            return len(self._linked_list)

    def enqueue(self, value):
        with self._lock:
            self._linked_list.append(value)

    def dequeue(self):
        with self._lock:
            return self._linked_list.remove(0).value

    def is_empty(self):
        with self._lock:
            return len(self._linked_list) == 0