#!/usr/bin/env python3
"""
pagination module
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters
    """

    start, end = 0, 0
    for x in range(page):
        start = end
        end += page_size
    return (start, end)
