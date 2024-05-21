#!/usr/bin/python3
"""Basic dictionary"""
from typing import Union

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching
    """
    def __init__(self):
        """Instantiates the class
        """
        super().__init__()

    def put(self, key: str, item: str) -> None:
        """Assigns the item value for the key to
        the dict cache_data"""
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key: str) -> Union[str, None]:
        """Retrieves the value in cache_data dict linked to key"""
        if key and key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
