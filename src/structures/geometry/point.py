from typing import NamedTuple
import math

Point = NamedTuple('Point', [('x', float), ('y', float)])


def is_counterclockwise(p1: Point, p2: Point, p3: Point):
    """
    Three points are a counter-clockwise turn if ccw > 0, clockwise if
    ccw < 0, and collinear if ccw = 0 because ccw is a determinant that
    gives twice the signed  area of the triangle formed by p1, p2 and p3.
    """
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def get_polar_angle(a: Point, b: Point):
    """
    Compute the polar angle between two points
    """
    return math.atan2(b.y - a.y, b.x - a.x)


def get_euclidian_distance(a: Point, b: Point):
    """
    Compute distance between two points
    """
    return math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))


def get_internal_angle(a: Point, b: Point, c: Point):
    """
    Compute the inner angle between [a, b] and [b, c]
    """
    ab = get_euclidian_distance(a, b)
    bc = get_euclidian_distance(b, c)
    ca = get_euclidian_distance(c, a)

    try:
        return math.acos(-1 * (math.pow(ca, 2) - math.pow(ab, 2) - math.pow(bc, 2)) / (2 * ab * bc)) * (180 / math.pi)
    except ValueError:
        return 180
