from src.structures import LinkedList, LinkedListNode, BinomialTreeNode, Stack


class FibonacciHeap(object):

    def __init__(self, data=None):
        if not data:
            data = []

        self.trees = LinkedList()

        self.min_tree = None

        for i in data:
            self.insert(i)

    def insert(self, value):
        tree = BinomialTreeNode(value)
        tree.marked = False

        self.trees.append(tree)

        # Update the min node reference if needed
        if self.min_tree is None or self.min_tree.value.value > value:
            self.min_tree = self.trees.get_tail_node()

    def pop(self):
        """
        Remove the minimum node from the heap
        Actual cost. O(rank(H)) + O(trees(H))
        * O(rank(H)) to meld min's children into root list.
        * O(rank(H)) + O(trees(H)) to update min.
        * O(rank(H)) + O(trees(H)) to consolidate trees.
        """
        if not self.min_tree:
            raise IndexError()
        value = self.min_tree.value.value

        for child in self.min_tree.value.children:
            self.trees.append(child)

        self.min_tree.value = None
        self.min_tree = None

        self.consolidate()

        return value

    def merge(self, heap: 'FibonacciHeap'):
        if len(self.trees) == 0:
            self.trees = heap.trees

        self.trees.merge(heap.trees)
        if heap.min_tree and (self.min_tree is None or heap.min_tree.value.value < self.min_tree.value.value):
            self.min_tree = heap.min_tree

    def decrease_min(self, node: BinomialTreeNode, value):
        if node.value < value:
            raise ValueError('Value should be smaller than this value')

        parent = node.parent

        while parent:

            # Remove node from parent and add it to the tree list
            parent.children.remove(node)
            node.parent = None
            self.trees.append(node)
            node.marked = False

            if self.min_tree is None or self.min_tree.value > node.value:
                self.min_tree = self.trees.get_tail_node()

            # Mark the parent
            if parent.marked:
                pass
                # Todo: finish decrease min

    # Utility functions
    def consolidate(self):
        """
        Restructure the tree back to a binomial tree
        """
        trees_by_rank = {}
        tree_stack = Stack()

        for tree in self.trees:
            tree_stack.push(tree)

        # Iterate over the trees and merge trees of the same rank
        while not tree_stack.is_empty():
            tree = tree_stack.pop()

            if tree is None:
                continue

            if tree.rank in trees_by_rank:
                existing_tree = trees_by_rank[tree.rank]
                del trees_by_rank[tree.rank]
                tree_stack.push(tree.merge_min(existing_tree))

            else:
                trees_by_rank[tree.rank] = tree

        # Build a new tree list and find the new min node
        new_trees = trees_by_rank.values()
        self.trees = LinkedList()
        self.min_tree = None

        for new_tree in new_trees:
            self.trees.append(new_tree)
            if self.min_tree is None or self.min_tree.value.value > new_tree.value:
                self.min_tree = self.trees.get_tail_node()

    def number_of_trees(self):
        return len(self.trees)

    def get_max_rank(self):
        if self.trees.get(0):
            return max(map(lambda x: x.rank, self.trees))

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

    def __len__(self):
        return sum(map(lambda x: len(x) if x else 0, self.trees))

    def is_empty(self):
        return self.min_tree is None
