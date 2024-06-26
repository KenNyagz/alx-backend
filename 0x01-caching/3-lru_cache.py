#!/usr/bin/env python3
'''
Caching that uses the Least Recently Used mechanism
'''
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''Lease Recently Used eviction mechanism in caching'''
    def __init__(self):
        '''init/constructor method'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Add an item by key'''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = next(iter(self.cache_data))
            print(f"DISCARD: {oldest_key}")
            self.cache_data.pop(oldest_key)

    def get(self, key):
        '''Get an item key'''
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
