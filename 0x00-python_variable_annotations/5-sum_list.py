#!/usr/bin/env python3
"""the `5-sum_list` module
defines the function `sum_list`
"""
from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns the sum of `input_list` elements as a float"""
    return reduce(lambda x, y: x + y, input_list)
