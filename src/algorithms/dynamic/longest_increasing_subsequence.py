import math


def longest_increasing_subsequence(numbers):
    """
    Finds the longest increasing subsequence for the given array
    :param numbers:
    """

    if not numbers:
        return []

    # Sub-sequence successor
    P = [None] * len(numbers)

    # Last element of the subsequence with a given lenght
    M = [None] * len(numbers)

    longest_length = 1
    M[0] = 0

    for i in range(1, len(numbers)):

        # Binary search over M
        low, high = 0, longest_length

        while low < high:
            middle = math.ceil((low + high)/2)

            if numbers[M[middle - 1]] < numbers[i]:
                low = middle
            else:
                high = middle - 1

        # Predecessor of i is the end of the longest subsequence smaller than numbers[i]
        P[i] = M[low - 1]

        # If the new subsequence is longer than the current longest subsequence or it is equal but the last
        # element is smaller, set the current subsequence as the longest
        if low == longest_length or numbers[M[low]] > numbers[i]:
            longest_length = max(longest_length, low + 1)
            M[low] = i

    # Build the longest subsequence from the predecessor list P
    longest_subsequence = []

    i = M[longest_length - 1]

    for _ in range(longest_length - 1):
        longest_subsequence.append(numbers[i])
        i = P[i]
    longest_subsequence.append(numbers[i])
    longest_subsequence.reverse()

    return longest_subsequence

