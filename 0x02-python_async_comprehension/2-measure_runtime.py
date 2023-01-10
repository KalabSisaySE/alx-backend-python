#!/usr/bin/env python3
"""the `2-measure_runtime` module
defines the function `measure_runtime`
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """runs `async_comprehension` 4 times and returns the total runtime"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
