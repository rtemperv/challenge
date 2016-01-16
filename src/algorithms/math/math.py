

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
