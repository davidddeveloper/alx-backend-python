#!/usr/bin/env python3
"""
    6-sum_mixed_list.py: Complex types - mixed list

"""
from typing import List
from functools import reduce


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
        - Attributes:
            - mxd_lst: list of integers and float

        - Return: sum of mxd_lst

    """

    return reduce(lambda x, y: x + y, mxd_lst)
