#!/usr/bin/python3
"""LFU Caching"""
from typing import Union

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A LFU algorithm caching system
    """
    counter = {}

    def __init__(self):
        """Instantiates the class
        """
        super().__init__()

    def put(self, key: str, item: str) -> None:
        """Assigns the item to key in cache_data dict"""
        if key and item:
            if len(list(self.cache_data.keys())) == self.MAX_ITEMS:
                sorted_counter = dict(sorted(self.counter.items(),
                                      key=lambda item: item[1],
                                      reverse=True))
                keys = list(sorted_counter.keys())
                del self.cache_data[keys[-1]]
                del self.counter[keys[-1]]
                print("DISCARD: {}".format(keys[-1]))

            self.cache_data.update({key: item})
            self.counter.update({key: self.MAX_ITEMS})

    def get(self, key: str) -> Union[str, None]:
        """Retrives the value linked to key if exists in cache_data
        """
        if key and key in self.cache_data.keys():
            if key in self.counter.keys():
                val = self.counter.get(key) + 1
                self.counter.update({key: val})
            return self.cache_data.get(key)
        return None
