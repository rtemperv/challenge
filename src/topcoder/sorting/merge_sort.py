

def merge_sort(array):
    """
    Simple merge sort implementation (n log n)
    """
    if len(array) < 2:
        return array

    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    result = []

    while True:

        if not left:
            return result + left

        if not right:
            return result + right

        if left[0] < right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]