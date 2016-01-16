

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
        return a * exponentiation_by_squaring((n-1)/2, a**2)

    else:
        return exponentiation_by_squaring(n/2, a**2)
