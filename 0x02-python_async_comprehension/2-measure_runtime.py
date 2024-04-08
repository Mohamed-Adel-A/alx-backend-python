#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
from time import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime for executing async_comprehension
    four times in parallel
    """
    start_time = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time()
    return end_time - start_time
