#!/usr/bin/env python3
"""the `8-make_multipler` module
defines the function `make_multiplier`
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
