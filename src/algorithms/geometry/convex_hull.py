from typing import List, NamedTuple
from src.structures import Stack, BinomialHeap
import math
import copy
Point = NamedTuple('Point', [('x', float), ('y', float)])


def jarvis(points: List) -> List[Point]:
    """
    In computational geometry, the gift wrapping algorithm is an algorithm
    for computing the convex hull of a given set of points.
    Complexity: O(nh)
    :return: the set of points which span the convex hull
    """

    # Take the leftmost point as the starting point of the hull
    leftmost_point = last_point = min(points, key=lambda point: point.x)
    current_point = max(points, key=lambda x: get_polar_angle(last_point, x))

    result = [leftmost_point]

    # Keep tracking the convex hull clockwise
    while current_point != leftmost_point:

        result.append(current_point)

        # Choose the point which result in the largest inner angle
        new_point = max(points, key=lambda x: get_internal_angle(last_point, current_point, x) if x != current_point else 0)

        last_point, current_point = current_point, new_point

    return result


def graham(points: List) -> List:
    """
    Graham's scan is a method of finding the convex hull of a finite
    set of points in the plane with time complexity O(n log n).
    It is named after Ronald Graham, who published the original
    algorithm in 1972.The algorithm finds all vertices of the
    convex hull ordered along its boundary.
    """
    points = points.copy()

    # Find the bottom left point and remove it from the set
    bottom_left_point = min(points, key=lambda x: (x[1], x[0]))
    points.remove(bottom_left_point)

    # Put the points on a min heap by polar angle
    polar_points = list(map(lambda x: (get_polar_angle(bottom_left_point, x), x), points))
    point_heap = BinomialHeap(polar_points)

    # Push the first 3 elements on a stack
    stack = Stack()
    stack.push(bottom_left_point)
    stack.push(point_heap.pop()[1])
    stack.push(point_heap.pop()[1])

    for _ in range(len(point_heap)):
        _, p3 = point_heap.pop()
        while is_counterclockwise(stack.peek(1), stack.peek(), p3) < 0:
            stack.pop()
        stack.push(p3)

    return stack.to_array()


def is_counterclockwise(p1, p2, p3):
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


def get_distance(a: Point, b: Point):
    """
    Compute distance between two points
    """
    return math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2) )


def get_internal_angle(a: Point, b: Point, c: Point):
    """
    Compute the inner angle between [a, b] and [b, c]
    """
    ab = get_distance(a, b)
    bc = get_distance(b, c)
    ca = get_distance(c, a)

    try:
        return math.acos(-1 * (math.pow(ca, 2) - math.pow(ab, 2) - math.pow(bc, 2))/(2*ab*bc)) * (180 / math.pi)
    except ValueError:
        return 180
