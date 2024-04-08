#!/usr/bin/env python3
"""
Tasks
"""

import asyncio
from typing import List, Task

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates asyncio Tasks for wait_random and returns the list of delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]