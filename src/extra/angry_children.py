import sys


def min_unfairness(candies, nr_of_children):

    while len(candies) < nr_of_children:
        candies.append(0)

    candies.sort()

    min_distance = sys.maxsize

    for i in range(len(candies) - nr_of_children + 1):
        min_distance = min(min_distance, candies[i + nr_of_children - 1] - candies[i])




