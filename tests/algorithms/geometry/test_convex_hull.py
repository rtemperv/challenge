from src.algorithms.geometry.convex_hull import jarvis, graham
from src.structures import Point
import unittest
import random


class TestConvexHull(unittest.TestCase):

    def setUp(self):
        self.points = [Point(-1, 0), Point(1, 1), Point(0, 1), Point(1, 0), Point(0.5, 0.5)]

    def test_jarvis(self):
        hull = jarvis(self.points)
        assert len(hull) == 4

        self.points.append(Point(2, 2))
        self.points.append(Point(0, -2))
        hull = jarvis(self.points)

        assert hull == [Point(-1, 0), Point(0, 1), Point(2, 2), Point(1, 0), Point(0, -2)]

    def test_graham_scan(self):

        hull = graham(self.points)
        assert len(hull) == 4

        self.points.append(Point(2, 2))
        self.points.append(Point(0, -2))
        hull = graham(self.points)

        assert set(hull) == {Point(-1, 0), Point(0, 1), Point(2, 2), Point(1, 0), Point(0, -2)}

    def plot_hull(self):
        import matplotlib.pyplot as plt
        points = []
        for _ in range(100):
            points.append(Point(random.random() * 10, random.random() * 10))

        hull = graham(points)

        for point in points:
            if point not in hull:
                plt.plot(point.x, point.y, 'bx')

        hull.append(hull[0])

        plt.plot([point.x for point in hull], [point.y for point in hull], 'ro-')

        plt.ylim((-2, 12))
        plt.xlim((-2, 12))
        plt.show()
