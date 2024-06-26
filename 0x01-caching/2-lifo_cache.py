#!/usr/bin/env python3
'''
LIFO eviction caching
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''lifo caching method'''
    def __init__(self):
        '''Constructor method'''
        super().__init__()

    def put(self, key, item):
        '''Add an item by key'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_elem = self.cache_data.popitem()
            print(f"DISCARD: {last_elem[0]}")
        self.cache_data[key] = item

    def get(self, key):
        '''Get an item key'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
