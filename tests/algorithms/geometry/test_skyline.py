from src.algorithms.geometry.skyline import build_skyline
import unittest


class TestSkyline(unittest.TestCase):
    def setUp(self):
        self.points = [(1, 20, 5), (10, 40, 2), (33, 54, 8), (38, 66, 6), (66, 70, 6)]

    def test_regular_skyline(self):

        assert build_skyline(self.points) == [(1, 0), (1, 5), (20, 5), (20, 2), (33, 2), (33, 8), (54, 8), (54, 6), (70, 6), (70, 0)]
