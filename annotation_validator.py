
from typing import Dict, List, Optional
from annotation.typed import typechecked, optional


@typechecked
def test(a, b: str, c: str='test') -> optional(int):
    pass


test(4, 'eee')