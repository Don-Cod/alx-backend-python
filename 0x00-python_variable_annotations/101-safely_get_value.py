#!/usr/bin/env python3
"""
Take parameters and values then add type annotations
to the function.
"""

from typing import Any, Union, Mapping, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """safely_GET_value"""
    if key in dct:
        return dct[key]
    else:
        return default
