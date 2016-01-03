from annotation.typed import typechecked


@typechecked
def is_rotation(a: str, b: str) -> bool:

    if len(a) != len(b):
        return False

    return a in (b + b)