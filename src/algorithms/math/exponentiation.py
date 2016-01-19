import numpy as np


def exponentiation_by_squaring(n, a):
    """
    Computes a^n using recursive exponentiation by squaring
    Basic idea:
        | x * (x^2)^((n-1)/2) if x is uneven
    x^n |
        | (x^2)^(n/2) if x is even
    """
    if n == 0:
        return 1

    if n == 1:
        return a

    if n % 2 == 1:
        if isinstance(a, int):
            return a * exponentiation_by_squaring((n-1)/2, a**2)
        if isinstance(a, np.ndarray):
            return np.dot(a, exponentiation_by_squaring((n - 1) / 2, np.dot(a, a)))

    else:
        if isinstance(a, int):
            return exponentiation_by_squaring(n/2, a**2)
        if isinstance(a, np.ndarray):
            return exponentiation_by_squaring(n / 2, np.dot(a, a))
