#!/usr/bin/env python3
"""
    3-tasks.py: asyncio.Task

"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
        Return: asyncio.Task

    """

    return asyncio.Task(wait_random())
