from typing import List


def insertion_sort(array: List):
    """
    In order sort of the array with time complexity of O(n2)
    """
    if len(array) < 2:
        return

    for index, element in enumerate(array):

        while index > 0:
            if array[index] < array[index - 1]:
                array[index], array[index - 1] = array[index - 1], array[index]
            else:
                break
            index -=1
