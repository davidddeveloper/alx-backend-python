#!/usr/bin/env python3
"""
    2-measure_runtime.py: Run time for four parallel comprehensions

"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        execute async_comprehension four times in parallel

        Return: the total runtime

    """

    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    return time.perf_counter() - start
