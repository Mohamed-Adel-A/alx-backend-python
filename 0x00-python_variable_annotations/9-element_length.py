#!/usr/bin/env python3
"""0x00-python_variable_annotations/9-element_length.py"""


from typing import Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing elements and their lengths."""
    return [(i, len(i)) for i in lst]
