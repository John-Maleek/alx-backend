#!/usr/bin/env python3
"""Module defines a server class with pagination"""


import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        return a tuple of size two containing a start
        index and an end index corresponding to the
        range of indexes to return in a list for
        those particular pagination parameters
    """
    start_index: int = 0
    end_index: int = 0

    for i in range(page):
        start_index = end_index
        end_index += page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Args:
                page(int): requested page (must be positive value > 0)
                page_size(int): number of items per
                page(must be postive value > 0)
            Return:
                list of list containing required data
        """
        assert type(page) is int and type(page_size) is int\
            and page > 0 and page_size > 0

        data: List[List] = self.dataset()
        try:
            index: int = index_range(page, page_size)
            return data[index[0]: index[1]]
        except IndexError or TypeError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            Args:
            page(int): requested page
            page_size(int): number of items per page
            Return:
            dict with key-value pairs
        """
        data: List[List] = self.get_page(page, page_size)
        total_pages: int = math.ceil(len(self.dataset()) / page_size)
        if len(data) == 0 or data == []:
            page_size = 0

        next_page: int = None if page > total_pages else page + 1
        prev_page: int = page - 1 if page > 1 else None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
            }
