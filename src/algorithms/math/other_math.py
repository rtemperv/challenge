import numpy as np
from src.algorithms.math.exponentiation import exponentiation_by_squaring


def gcd(a: int, b: int) -> int:
    """
    Find the greatest common divisor between two values
    """
    if a % b == 0:
        return b

    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    """
    Find the lowest common denominator
    """

    return (a * b) / gcd(a, b)


def nth_fibonacci(n: int) -> int:
    """
    Find the nth fibonacci number using matrix factorization
    Time complexity: O(log n)
    """

    if n == 0 or n == 1:
        return 1

    initial_state = np.array([1, 1])

    transformation_matrix = np.array([[0, 1], [1, 1]])
    result = np.dot(initial_state, exponentiation_by_squaring(n - 1, transformation_matrix))

    return result[1]
