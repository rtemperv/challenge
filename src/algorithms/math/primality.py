import math

import random


def miller_rabin(n, precision=4):
    """
    Miller rabin test for a given number n and a given precision
    """

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient

    assert (2 ** s * d == n - 1)

    for _ in range(precision):

        a = random.randint(2, n - 2)

        x = (a ** d) % n

        if x == 1 or x == n - 1:
            continue

        for r in range(s - 1):

            x = (x ** 2) % n
            if x == 1:
                return False

            if x == n - 1:
                a = 0
                break
        if a:
            return False
    return True


def exhaustive_is_prime(n):
    for i in range(1, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True
