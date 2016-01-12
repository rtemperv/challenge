from typing import List, NamedTuple
import math
Point = NamedTuple('Point', [('x', float), ('y', float)])


def jarvis(points: List) -> List[Point]:
    """
    In computational geometry, the gift wrapping algorithm is an algorithm
    for computing the convex hull of a given set of points.
    :return: the set of points which span the convex hull
    """

    # Take the leftmost point as the starting point of the hull
    leftmost_point = last_point = min(points, key=lambda point: point.x)
    current_point = max(points, key=lambda x: get_angle(last_point, x) + 90)

    result = [leftmost_point]

    # Keep tracking the convex hull clockwise
    while current_point != leftmost_point:

        result.append(current_point)

        # Choose the point which result in the largest inner angle
        new_point = max(points, key=lambda x: get_internal_angle(last_point, current_point, x) if x != current_point else 0)

        last_point, current_point = current_point, new_point

    return result


def get_angle(a: Point, b: Point):
    return math.atan2(b.y - a.y, b.x - a.x) * (180 / math.pi)

def get_distance(a: Point, b: Point):
    return math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2) )


def get_internal_angle(a: Point, b: Point, c: Point):
    ab = get_distance(a, b)
    bc = get_distance(b, c)
    ca = get_distance(c, a)

    try:
        return math.acos(-1 * (math.pow(ca, 2) - math.pow(ab, 2) - math.pow(bc, 2))/(2*ab*bc)) * (180 / math.pi)
    except ValueError:
        return 180
