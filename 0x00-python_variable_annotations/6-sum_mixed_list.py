#!/usr/bin/env python3
"""
Write a type-annotated function and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sums list_integers and floats """
    return sum(mxd_lst)
