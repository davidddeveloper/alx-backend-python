#!/usr/bin/env python3
"""
    7-to_kv.py: Complex types - string and int/float to tuple

"""
from typing import Tuple

def to_kv(k: str, v: int | float) -> Tuple(str, float):
    """
        - Args:
            - k: the string
            - v: int or float

        - Return: tuple of int and float

    """

    return (k, v ** 2)
