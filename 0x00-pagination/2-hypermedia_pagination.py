#!/usr/bin/env python3
"""Simple helper function"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
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
        assert (type(page) is int)
        assert (type(page_size) is int)
        assert (page > 0)
        assert (page_size > 0)
        index_rg = index_range(page, page_size)
        data_set = self.dataset()
        if index_rg[0] > len(data_set) or index_rg[1] > len(data_set):
            return []

        return data_set[index_rg[0]:index_rg[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        data = self.get_page(page, page_size)
        total_pages = int(len(self.dataset()) / page_size)
        if page + 1 < total_pages:
            n_page = page + 1
        else:
            n_page = None
        # n_page = page++ < total_pages? page + 1: None
        if page > 1:
            p_page = page - 1
        else:
            p_page = None
        # p_page = page > 0? page - 1: None

        return {"page_size": page_size, "page": page, "data": data,
                "next_page": n_page, "prev_page": p_page,
                "total_pages": total_pages}
