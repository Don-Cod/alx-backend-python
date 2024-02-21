#!/usr/bin/env python3
"""
A type-annotated function & second element is the square of the
int/float v and should be annotated as a float.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A string int or float & returns a tuple"""
    return (k, v ** 2)
