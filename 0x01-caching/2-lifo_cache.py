#!/usr/bin/env python3
""" LIFO Caching """

from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Caching system with LIFO startegy """

    def __init__(self):
        """ init method """
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """ Insert into caching new key and item """

        # If key or item is None, this method should not do anything.
        if key is None or item is None:
            return

        # Update the item value if key already exists
        if key in self.cache_data:
            self.order.remove(key)

        # LIFO eviction if cache limit is reached
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            del_item = self.order.pop()
            del self.cache_data[del_item]
            print(f"DISCARD: {del_item}")

        # Insert the new key-value pair
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve a value from the cache"""
        return self.cache_data.get(key)
