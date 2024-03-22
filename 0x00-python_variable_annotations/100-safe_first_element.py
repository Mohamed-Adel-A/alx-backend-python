#!/usr/bin/env python3
"""0x00-python_variable_annotations/100-safe_first_element.py"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """Returns the first element of a sequence if it exists, otherwise None."""
    if lst:
        return lst[0]
    else:
        return None
