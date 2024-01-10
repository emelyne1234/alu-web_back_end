#!/usr/bin/env python3
"""returning the appropriate types"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
"""returns values with the appropriate types"""
    return [(i, len(i)) for i in lst]
