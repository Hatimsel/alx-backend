#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        if index:
            assert (index < len(self.indexed_dataset()))
            page = int(index / page_size)
        else:
            page = 1

        last_index = index + page_size
        # data = [self.indexed_dataset()[i] for i in range(index, last_index)]
        data = []
        for i in range(index, last_index):
            if i in self.indexed_dataset().keys():
                data.append(self.indexed_dataset()[i])
            else:
                data.append(self.indexed_dataset()[i + 1])
                last_index += 1
        # data = self.indexed_dataset()[index:last_index]
        return {"index": index, "next_index": index + page_size,
                "page_size": page_size, "data": data}
