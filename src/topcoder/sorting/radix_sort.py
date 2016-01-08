from typing import List
from itertools import chain


def radix_sort(array: List, fn=lambda x: x):
    """
    Radix sort implementation using merge sort
    @param fn: function to transform elements from the list to integers
    """
    RADIX = 10

    divisor = 1

    while True:
        nodes_by_index = [[] for i in range(RADIX)]

        for i in array:
            value = fn(i) // divisor
            index = value % RADIX
            nodes_by_index[index].append(i)

        # Rebuild array
        array = list(chain(*nodes_by_index))

        # Stop if all elements are in the same bucket
        if len(list(filter(lambda x: len(x) > 0, nodes_by_index))) <= 1:
            break

        divisor *= RADIX

    return array
