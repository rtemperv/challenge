

class BinomialTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None  # type: BinomialTreeNode

    def __len__(self):
        return 1 + sum(map(lambda x: len(x) if x else 0, self.children))

    @property
    def rank(self):
        return len(self.children)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def merge_min(self, a: 'BinomialTreeNode') -> 'BinomialTreeNode':
        """
        Merge two binomial trees such that the minimal element is the root
        """
        if a.value < self.value:
            a.add_child(self)
            return a
        else:
            self.add_child(a)
            return self