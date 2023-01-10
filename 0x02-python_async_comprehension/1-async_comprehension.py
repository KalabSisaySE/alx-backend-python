#!/usr/bin/env python3
"""the `1-async_comprehension` module
defines the function `async_comprehension`
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """uses async comprehension and returns a list of 10 random numbers"""
    return [num async for num in async_generator()]
