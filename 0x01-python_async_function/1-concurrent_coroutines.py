#!/usr/bin/env python3
"""
    1-concurrent_coroutines.py:
    execute multiple coroutines at the same time with async

"""

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        async routine that return the list of all the delays by wait_random
    """

    delays: list = []
    for _ in range(n):
        delay: float = await wait_random(max_delay)
        delays.append(delay)

    return delays
