
def is_unique(x: str):
    if not isinstance(x, str):
        raise ValueError()

    if x is None or len(x) == 0:
        return True

    x_sorted = sorted(x.lower())
    tmp_char = x_sorted[0]
    for i in x_sorted[1:]:
        if i == tmp_char:
            return False
        tmp_char = i
    return True
