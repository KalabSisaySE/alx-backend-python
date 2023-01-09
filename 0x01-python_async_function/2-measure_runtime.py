#!/usr/bin/env python3
"""the `2-measure_runtime` module
defines the function `measure_time`
"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns the total execution time for `wait_n`"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - start) / n
