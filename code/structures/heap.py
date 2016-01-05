from code.structures import Queue, BinaryNode


class BinaryHeap(object):
    """
    Binary heap implementation based on BinaryTree
    """

    def __init__(self, data=None):

        if data:
            self.q = Queue()

            # First build a random binary tree from the data
            self._root = BinaryNode(data[0])

            q.enqueue(self._root)

            for i in data:
                self.__add_as_leaf(i)

    def __add_as_leaf(self, value):
        current_node = self.q.peek()

        if not current_node.lvalue:
            current_node.lvalue = BinaryNode(value)
            self.q.enqueue(current_node.lvalue)
        else:
            current_node.rvalue = BinaryNode(value)
            self.q.enqueue(current_node.rvalue)
            self.q.dequeue()

    def peek(self):
        return self._root.value if self._root else None

    def pop(self):
        value = self.peek()
        if self._root:
            self.__extract(self._root)
        return value

    def __extract(self, node):
        

    def heapify(self, l):
        pass
