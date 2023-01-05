#!/usr/bin/env python3
"""the `9-element_length` module
defines the function `element_length`
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples from the elements of `lst`"""
    return [(i, len(i)) for i in lst]
