#!/usr/bin/env python3
"""
    1-concurrent_coroutines.py:
    execute multiple coroutines at the same time with async

"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
        async routine that return the list of all the delays by wait_random
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    return delays
