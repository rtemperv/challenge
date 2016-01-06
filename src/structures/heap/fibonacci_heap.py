from src.structures import LinkedList, LinkedListNode

class fibonacci_heap(object):

    def __init__(self, data=None):
        if not data:
            data = []

        self.trees = LinkedList()
        self.min