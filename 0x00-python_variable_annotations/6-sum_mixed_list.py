#!/usr/bin/env python3
"""the `6-sum_mixed_list` module
defines the function `sum_mixed_list`
"""
from functools import reduce
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of the elements of `mxd_lst`"""
    return reduce(lambda x, y: x + y, mxd_lst)
