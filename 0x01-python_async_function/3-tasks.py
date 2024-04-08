#!/usr/bin/env python3
"""
Tasks
"""

import asyncio
from typing import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Creates an asyncio Task for wait_random
    """
    return asyncio.create_task(wait_random(max_delay))
