#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """Takes two arguments
    page: the page number
    page_size: the page size
    Returns a tuple of size two containing the start
    and end indices"""
    end = page * page_size
    start = end - page_size

    return (start, end)
