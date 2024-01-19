#!/usr/bin/env python3
"""simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size two containing a start index and end index"""
    start_index = page * page_size - page_size
    end_index = start_index + page_size
    return (start_index, end_index)
