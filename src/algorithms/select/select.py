from typing import List
from src.structures.heap import BinomialHeap


def quick_select(array: List, k: int):
    """
    Find the k smallest item in the list through deterministic quick select
    Average: O(n) Worst case: O(n2)
    """
    if len(array) <= k:
        return None

    pivot = array[0]

    smaller = [i for i in array if i < pivot]
    larger = [i for i in array if i >= pivot]

    if len(smaller) == k:
        return pivot
    if k > len(smaller):
        return quick_select(larger[1:], k - len(smaller) - 1)
    if k < len(smaller):
        return quick_select(smaller, k)


def heap_smallest(array: List, k: int):
    """
    Find k smallest based on Binomial heap implementation
    O(n + k log n)
    """
    heap = BinomialHeap(array)

    try:

        [heap.pop() for _ in range(k)]
        return heap.pop()

    except IndexError:
        return None

