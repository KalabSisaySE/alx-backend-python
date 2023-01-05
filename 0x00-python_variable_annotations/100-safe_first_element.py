#!/usr/bin/env python3
"""the `100-safe_first_element` module
defines the function `safe_first_element`
"""
from typing import Iterable, Union, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Iterable[Any]) -> Union[Any, None]:
    """if `lst` is a `list` returns first element else `None`"""
    if lst:
        return lst[0]
    else:
        return None