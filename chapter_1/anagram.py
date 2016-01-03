from annotation.typed import typechecked


@typechecked
def is_anagram(a: str, b: str) -> bool:
    return a == b[::-1]