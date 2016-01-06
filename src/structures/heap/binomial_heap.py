from src.structures import BinomialTreeNode
from src.structures.linked_list import LinkedList, LinkedListNode
from typing import List, Optional
import math


class BinomialHeap(object):

    def __init__(self, data=None):
        """
        Build a binomial heap from the provided dataset
        """
        if data is None:
            data = []

        self.trees = LinkedList()
        self.trees.append(None)

        # Pointer to the minimal tree
        self.min_tree = None

        for i in data:
            self.insert(i)

    def merge(self, heap: 'BinomialHeap') -> 'BinomialHeap':
        """
        Bread and butter of the binomial heap
        Merges two binomial heaps in O(log n)
        """
        # Initialize head pointers
        carry_over = None
        destination_heap = self.trees.head
        source_heap = heap.trees.head

        # Keep merging while the source heap is not empty or we have a carry over
        while source_heap or carry_over:

            # Both source and destination heap have an element of this order
            if destination_heap is not None and destination_heap.value and source_heap is not None and source_heap.value:
                new_carry_over = self.__merge_trees(destination_heap.value, source_heap.value)
                destination_heap.value = carry_over if carry_over else None
                carry_over = new_carry_over

            # Only the source heap has an element of this order
            elif source_heap is not None and source_heap.value:
                if carry_over:
                    carry_over = self.__merge_trees(carry_over, source_heap.value)
                    destination_heap.value = None
                else:
                    destination_heap.value = source_heap.value

            # Only the destination heap has an element of this order
            elif destination_heap is not None and destination_heap.value:
                if carry_over:
                    carry_over = self.__merge_trees(carry_over, destination_heap.value)
                    destination_heap.value = None

            # Only carry over
            else:
                destination_heap.value = carry_over
                carry_over = None

            # Increase the pointers and add an extra element to the linked list if needed
            source_heap = source_heap.get_next_node() if source_heap else None
            if (source_heap or carry_over) and destination_heap.get_next_node() is None:
                destination_heap.set_next_node(LinkedListNode(None))
            destination_heap = destination_heap.get_next_node() if destination_heap else None

        # Update min pointer
        self.min_tree = self.__find_min_tree()

    def insert(self, value):
        """
        Insert a value onto the heap
        Merges this heap with a new heap with only one node
        """
        # Create a heap with a single node
        new_heap = BinomialHeap()
        new_heap.trees.head.value = BinomialTreeNode(value)
        new_heap.min_tree = new_heap.trees.head
        # Merge it with the current heap
        self.merge(new_heap)

    def pop(self):
        """
        Remove and return the minimal node from the heap
        Creates a new heap from the
        """
        if self.min_tree is None or self.min_tree.value is None:
            raise IndexError()

        minimum = self.min_tree.value.value
        subtrees = self.min_tree.value.children
        self.min_tree.children = None
        self.min_tree.value = None

        heap = self.__build_heap_from_trees(subtrees)
        self.merge(heap)

        return minimum

    def peek(self):
        if self.min_tree is None:
            raise IndexError()
        return self.min_tree.value.value

    def __len__(self):
        return sum(map(lambda x: len(x) if x else 0, self.trees.to_array()))

    @staticmethod
    def __merge_trees(a: BinomialTreeNode, b: BinomialTreeNode) -> BinomialTreeNode:
        """
        Merge two binomial trees such that the minimal element is the root
        """
        if a.value < b.value:
            a.add_child(b)
            return a
        else:
            b.add_child(a)
            return b

    @staticmethod
    def __build_heap_from_trees(trees: List[Optional[BinomialTreeNode]]) -> 'BinomialHeap':
        """
        Build a new heap from an array of Binomial trees
        """
        trees.sort(key=lambda x: len(x))

        heap = BinomialHeap()
        current_node = heap.trees.head
        heap_size = 1

        for i in trees:
            index = math.log(len(i), 2)

            while heap_size <= index:
                current_node.set_next_node(LinkedListNode(None))
                current_node = current_node.get_next_node()
                heap_size += 1
            current_node.value = i

        heap.min_tree = heap.__find_min_tree()
        return heap

    def __find_min_tree(self) -> LinkedListNode:
        """
        Find the binomial subtree with the minimal element
        """
        node = self.trees.head

        current_min = None

        while node:
            if node.value and node.value.value:
                if current_min and current_min.value:
                    current_min = node if current_min.value.value > node.value.value else current_min
                else:
                    current_min = node
            node = node.get_next_node()
        return current_min
