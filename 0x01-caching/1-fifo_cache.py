#!/usr/bin/env python3
""" FIFO caching """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Cache system """

    def __init__(self):
        """init method"""
        super().__init__()
        self.cache_data = {}
