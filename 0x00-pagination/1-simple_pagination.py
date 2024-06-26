#!/usr/bin/env python3
"""Simple helper function"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Takes two arguments
    page: the page number
    page_size: the page size
    Returns a tuple of size two containing the start
    and end indices"""
    end = page * page_size
    start = end - page_size

    return (start, end)


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
        """Returns a page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        index_rg = index_range(page, page_size)
        data_set = self.dataset()

        if index_rg[0] >= len(data_set):
            return []

        return data_set[index_rg[0]:index_rg[1]]
