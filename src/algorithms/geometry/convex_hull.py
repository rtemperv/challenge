from typing import List
from src.structures import Stack, BinomialHeap
from src.structures import Point
from src.structures.geometry.point import get_internal_angle, get_polar_angle, is_counterclockwise


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

    # Find the bottom left point and remove it from the set
    bottom_left_point = min(points, key=lambda x: (x[1], x[0]))

    # Put the points on a min heap by polar angle
    polar_points = [(get_polar_angle(bottom_left_point, x), x) for x in points if x != bottom_left_point]
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

