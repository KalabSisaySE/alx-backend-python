#!/usr/bin/env python3
"""the `7-to_kv` module
defines the function `to_kv`
"""
from math import pow
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of `k` and square of `v`"""
    return (k, pow(v, 2))
