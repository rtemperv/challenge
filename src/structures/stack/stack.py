from src.structures.linked_list import LinkedList
from threading import Lock


class Stack(object):
    """
    FILO queue based on single linked list
    All operations are O(1)
    """
    def __init__(self):
        # Use composition to hide the linked list implementation details
        self._linked_list = LinkedList()
        self._lock = Lock()

    def __len__(self):
        with self._lock:
            return len(self._linked_list)

    def __contains__(self, item):
        return item in self._linked_list

    def push(self, value):
        with self._lock:
            self._linked_list.prepend(value)

    def pop(self):
        with self._lock:
            return self._linked_list.remove(0).value

    def peek(self):
        with self._lock:
            return self._linked_list.get(0).value

    def is_empty(self):
        with self._lock:
            return len(self._linked_list) == 0

