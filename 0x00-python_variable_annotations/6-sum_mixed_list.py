#!/usr/bin/env python3
"""0x00-python_variable_annotations/6-sum_mixed_list.py"""


from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums up a list of integers and floats."""
    return sum(mxd_lst)
