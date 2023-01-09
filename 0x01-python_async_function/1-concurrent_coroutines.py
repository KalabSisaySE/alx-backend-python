#!/usr/bin/env python3
"""the `1-concurrent_coroutines` module
defines the function `wait_n`
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """invokes `wait_random` `n` times and returns the list of all delays"""
    res = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return res
