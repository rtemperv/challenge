import unittest
from src.structures import UnionFind


class TestUnionFind(unittest.TestCase):

    def setUp(self):
        self.uf = UnionFind(12)

    def test_union(self):
        self.uf.union(1, 3)
        self.uf.union(2, 8)
        self.uf.union(9, 1)
        self.uf.union(4, 5)
        self.uf.union(9, 5)
        self.uf.union(10, 11)

        assert self.uf.find(1) == self.uf.find(4)
        assert self.uf.find(10) != self.uf.find(8)
        assert self.uf.find(2) == self.uf.find(8)
        assert max(self.uf.ranks) == 3
