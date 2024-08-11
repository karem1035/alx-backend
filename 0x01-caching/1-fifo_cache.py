#!/usr/bin/env python3
""" FIFO caching """
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Cache system """

    def __init__(self):
        """init method"""
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """ puts new key and value on the cache system """
        # If key or item is None, this method should not do anything.
        if key is None or item is None:
            return

        # Update the item value if key already exists
        if self.cache_data.get(key):
            self.cache_data[key] = item
            return

        # if the cache is full, replace the first inserted key
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            del_item = self.order.popleft()
            del self.cache_data[del_item]
            print(f"DISCARD: {del_item}")

        # Adding the key and item to the cache,and the key to the order
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ retrive data cached """
        if key:
            return self.cache_data.get(key)
        return None
