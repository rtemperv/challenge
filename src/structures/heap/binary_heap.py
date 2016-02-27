from src.structures import BinaryNode


class BinaryHeap(object):
    """
    Binary min heap implementation based on BinaryTree
    """

    def __init__(self, data=None):
        if data is None:
            data = []

        self.heap_size = len(data)
        self._root = BinaryNode.from_array(data) # type: BinaryNode

        self.heapify()

    def peek(self):
        """
        Returns the minimal element of the heap and keeps the structure unchanged
        """
        if self._root is None:
            raise IndexError()
        return self._root.value

    def pop(self):
        if self._root is None:
            raise IndexError()
        
        last_node = self.__find_last_node()

        if self._root == last_node:
            self._root = None
        else:
            # Switch first and last node
            last_node.value, self._root.value = self._root.value, last_node.value

            if last_node.parent:
                if last_node.parent.lnode == last_node:
                    last_node.parent.lnode = None
                elif last_node.parent.rnode == last_node:
                    last_node.parent.rnode = None
            # Fix the heap constraints
            self.__percolate_down(self._root)

        self.heap_size -= 1

        return last_node.value

    def insert(self, value):
        """
        Insert a node at the bottom of the tree and percolate it up
        """
        parent = self.__find_new_parent()

        node = BinaryNode(value)

        if parent is None:
            self._root = node
        else:
            if parent.lnode:
                parent.rnode = node
            else:
                parent.lnode = node

        self.__percolate_up(node)

        self.heap_size += 1

    def heapify(self):
        """
        O(n) method to heapify a binary tree
        """
        if self._root is None:
            return

        for node in reversed(list(self._root.breadth_first_traversal())):
            if node.lnode or node.rnode:
                self.__percolate_down(node)

    def is_empty(self):
        return self._root is None

    def print(self):
        self._root.pretty_print()

    def __percolate_down(self, node: BinaryNode) -> None:
        """
        Bubble up heap operation
        """
        min_child = node.get_min_child()
        if min_child and min_child.value < node.value:
            node.value, min_child.value = min_child.value, node.value
            self.__percolate_down(min_child)

    def __percolate_up(self, node: BinaryNode) -> None:
        """
        Trickle down heap operation
        """
        if node.parent and node.parent.value > node.value:
            node.value, node.parent.value = node.parent.value, node.value
            self.__percolate_up(node.parent)

    def __find_last_node(self):
        """
        Find the parent node to insert a new node and keep the tree complete (O(logn))
        """
        return self.__find_node_at_position(self.heap_size)

    def __find_new_parent(self):
        """
        Find the parent node to insert a new node and keep the tree complete (O(logn))
        """
        return self.__find_node_at_position((self.heap_size + 1) // 2)

    def __find_node_at_position(self, position):

        node = self._root
        binary_representation = "{0:b}".format(position)[1:]

        for bit in binary_representation:
            if bit == "1":
                node = node.rnode
            else:
                node = node.lnode

        return node


class BinaryHeap2(object):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i //= 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
