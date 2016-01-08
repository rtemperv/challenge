

def quick_sort(array):

    if len(array) < 2:
        return array

    pivot = array[0]

    left_list = []
    right_list = []

    for element in array[1:]:
        if element < pivot:
            left_list.append(element)
        else:
            right_list.append(element)

    return quick_sort(left_list) + [pivot] + quick_sort(right_list)
