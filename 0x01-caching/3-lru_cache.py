#!/usr/bin/env python3
""" LRU Caching Implementation """

from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache Class

    Inherits from BaseCaching and implements a Least Recently Used (LRU)
    caching system. When the cache reaches its maximum capacity, the
    least recently used item is discarded.
    """

    def __init__(self):
        """Initialize the LRUCache.

        Initializes the cache and a deque to track the order of usage.
        """
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """Add an item to the cache.

        If the key already exists, update the value and mark it as the most
        recently used. If the cache exceeds its limit, the least recently used
        item is removed.

        Args:
            key: The key for the cache item.
            item: The value to be cached.

        Note:
            If either `key` or `item` is None, this method does nothing.
        """
        if not key or not item:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            del_item = self.order.popleft()
            del self.cache_data[del_item]
            print(f"DISCARD: {del_item}")

        # Insert or update the key-value pair
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve an item from the cache.

        If the key exists, the item is returned and the key is marked as the
        most recently used. If the key does not exist, None is returned.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The cached value associated with the key, or None if the key
            is not found.
        """
        if key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data.get(key)
