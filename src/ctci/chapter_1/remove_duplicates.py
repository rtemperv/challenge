from annotation.typed import typechecked

@typechecked
def remove_duplicates(x: str) -> str:
    """
    O(n2) implementation in place
    """
    if len(x) < 2:
        return x

    i = 1
    while i < len(x):
        if x[i] in x[:i]:
            x = x[:i] + x[i+1:]
            i -= 1
        i += 1
    return x


@typechecked
def remove_duplicates_better(x: str) -> str:
    """
    O(n) implementation with O(1) space for ascii strings
    """
    if len(x) < 2:
        return x

    i = 1 << ord(x[0])
    j = 1
    while j < len(x):
        if (1 << ord(x[j])) & i:
            x = x[:j] + x[j + 1:]
            j -= 1
        else:
            i |= 1 << ord(x[j])
        j += 1
    return x

