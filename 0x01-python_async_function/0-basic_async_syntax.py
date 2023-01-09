#!/usr/bin/env python3
"""the `0-basic_async_syntax` module
defines the function `wait_random`
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random seconds of max `max_delay` and returns the second"""
    sec = uniform(0, max_delay)
    await asyncio.sleep(sec)
    return sec
