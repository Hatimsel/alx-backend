#!/usr/bin/python3
"""FIFO Caching"""
from typing import Union

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO algorithm caching system
    """
    def __init__(self):
        """Instantiates the class
        """
        super().__init__()

    def put(self, key: str, item: str) -> None:
        """Assigns the item to key in cache_data dict"""
        if key and item:
            if len(list(self.cache_data.keys())) >= self.MAX_ITEMS:
                keys = list(self.cache_data.keys())
                del self.cache_data[keys[0]]
                print("DISCARD: {}".format(keys[0]))

            self.cache_data.update({key: item})

    def get(self, key: str) -> Union[str, None]:
        """Retrives the value linked to key if exists in cache_data
        """
        if key and key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
