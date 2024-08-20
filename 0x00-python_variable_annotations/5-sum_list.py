#!/usr/bin/env python3
"""
    5-sum_list.py: complex types - list of floats

"""
from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    """
        - Attributes:
            input_list: list of float

        - Return: the sum of input_list

    """

    return reduce(lambda x, y: x + y, input_list)
