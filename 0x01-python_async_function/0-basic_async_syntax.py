#!/usr/bin/env python3
"""
    0-basic_async_syntax.py: The basics of async

"""
import random

async def wait_random(max_delay: int = 10) -> float:
    """
        asynchronous coroutine that waits for a random delay
        and return random delay

    """

    random_value = random.randint(0, max_delay)
    await random_value
    return random_value
