

class BinomialTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.children = []

    def __len__(self):
        return 1 + sum(map(lambda x: len(x) if x else 0, self.children))

    def add_child(self, child):
        self.children.append(child)
