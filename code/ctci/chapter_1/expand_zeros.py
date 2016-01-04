from annotation.typed import typechecked, optional
from typing import List

@typechecked
def expand_zeros(matrix: List[List[int]]) -> type(None):

    height = len(matrix)
    width = len(matrix[0])

    rows = [False] * height
    columns = [False] * width

    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 0:
                rows[i] = True
                columns[j] = True

    for i in range(height):
        for j in range(width):
            if rows[i] or columns[j]:
                matrix[i][j] = 0



