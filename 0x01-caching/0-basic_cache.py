#!/usr/bin/env python3
"""Basic dictionary"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cache system
    """

    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """ puts new key and value on the cache system """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ retrive data cached """
        if key:
            return self.cache_data.get(key)
        return None
