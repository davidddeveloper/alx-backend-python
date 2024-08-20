#!/usr/bin/env python3
"""
    4-tasks.py: alter wait_n

"""

from typing import List
task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        async routine that return the list of all the delays by wait_random
    """

    return [await task_wait_random(max_delay) for _ in range(n)]
