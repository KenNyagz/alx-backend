#!/usr/bin/env python3
'''
cache class that uses the FIFO eviction mechanism
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''FIFO caching'''

    def put(self, key, item):
        '''Add an item in the cache'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f'DISCARD: {first_key}')
        self.cache_data[key] = item

    def get(self, key):
        '''Get an item by key'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
