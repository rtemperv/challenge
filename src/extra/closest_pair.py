
import sys


def find_closest_pair(arr1, arr2, x):
    """
    Find i and j such that arr1[i] + arr2[j] - x are minimal
    """

    if not arr1 or not arr2:
        return None

    i = 0
    j = 0

    turn = True
    last_minimum = abs(arr1[i] + arr2[j] - x)
    global_minimum = (last_minimum, i, j)

    while (i + 1 < len(arr1) ) or (j + 1 < len(arr2)):

        if turn and i + 1 < len(arr1):
            i += 1
        else:
            j += 1

        new_minimum = abs(arr1[i] + arr2[j] - x)

        if new_minimum > last_minimum:
            turn = not turn

        global_minimum = min((new_minimum, i, j), global_minimum)
        last_minimum = new_minimum

    return global_minimum



