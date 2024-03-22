#!/usr/bin/env python3

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier."""
    def multiplier_fn(n: float) -> float:
        return n * multiplier
    return multiplier_fn
