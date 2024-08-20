#!/usr/bin/env python3
"""
    8-make_multiplier.py: Complex types - functions

"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        - Args:
            - multiplier: float

        - Return: a function that multiplies a float by multiplier

    """

    def mp(mtip: float):
        return mtip * multiplier

    return mp
