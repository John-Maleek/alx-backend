#!/usr/bin/env python3
"""Module defines a simple helper function"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        return a tuple of size two containing a start
        index and an end index corresponding to the
        range of indexes to return in a list for
        those particular pagination parameters
    """
    start_index: int = 0
    end_index: int = 0

    for _ in range(page):
        start_index = end_index
        end_index += page_size
    return (start_index, end_index)
