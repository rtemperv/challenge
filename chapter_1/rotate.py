from annotation.typed import typechecked, optional
from typing import List


@typechecked
def rotate(matrix: List[List[optional(int)]]) -> List[List[optional(int)]]:

    if not is_square(matrix):
        raise ValueError()
    # Rotate 90 degrees
    # O(n) + O(n2) + O(n2)
    return list(map(list, zip(*matrix[::-1])))


@typechecked
def is_square(matrix: List[List[optional(int)]]) -> bool:
    # Check rows are of equal size O(n)
    width = None
    for i in matrix:
        if not width:
            width = len(i)
        elif width != len(i):
            return False

    # Rectangular matrix O(1)
    if width != len(matrix):
        return False

    return True