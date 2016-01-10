from src.structures.heap.binary_heap import BinaryHeap


def heap_sort(array):
    """
    Sorts an array using a binary heap in O(log n)
    """

    # In order transform to heap
    heap = BinaryHeap(array)

    for i in range(len(array)):
        array[i] = heap.pop()
