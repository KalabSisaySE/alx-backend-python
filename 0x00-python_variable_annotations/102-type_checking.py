#!/usr/bin/env python3
"""the 102-type_checking module
defines the functoin `zoom_array`
"""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """return a zoomed `lst` based on `factor`"""
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in
