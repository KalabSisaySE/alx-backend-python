#!/usr/bin/env python3
"""the `0-async_generator` module
defines the function async_generator
"""
import asyncio
from random import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """yields random numbers between 0 and 10"""
    for i in range(10):
        yield (random() * 10)
        await asyncio.sleep(1)
