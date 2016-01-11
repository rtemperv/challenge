

class UnionFind(object):
    """
    Union find implementation stored in an array with
    * by rank weighting
    * path compression
    """

    def __init__(self, n: int):
        """
        :param n: number of elements. Allows for the union of integers [0,n[
        """
        self.parent_references = list(range(n))
        self.ranks = [1] * n

    def union(self, a: int, b: int):
        """
        Merge sets containing a and b
        """

        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        if self.ranks[root_a] > self.ranks[root_b]:
            self.parent_references[root_b] = root_a
        if self.ranks[root_b] > self.ranks[root_a]:
            self.parent_references[root_a] = root_b
        else:
            self.parent_references[root_a] = root_b
            self.ranks[root_b] += 1

    def find(self, element: int):
        """
        Find the root of the given element and apply path compression
        """
        if self.parent_references[element] != element:
            self.parent_references[element] = self.find(self.parent_references[element])

        return self.parent_references[element]

