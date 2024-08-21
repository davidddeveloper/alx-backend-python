#!/usr/bin/env python3
"""
    0-async_generator.py: async generator

"""
import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """
        loop 10 times
        asynchronously wait 1 second
        yield a random number

    """

    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
