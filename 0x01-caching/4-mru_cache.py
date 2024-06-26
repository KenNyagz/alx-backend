#!/usr/bin/env python3
'''
Caching that uses the Least Recently Used mechanism
'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''Most Recently Used eviction mechanism in caching'''
    def __init__(self):
        '''init/constructor method'''
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        '''Add an item by key'''
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if key in self.mru_order:
            self.mru_order.remove(key)
        self.mru_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # most_recent_key = next(reversed(self.cache_data))
            most_recent_key = self.mru_order.pop(0)
            del self.cache_data[most_recent_key]
            print(f"DISCARD: {most_recent_key}")

    def get(self, key):
        '''Get an item key'''
        if key is None or key not in self.cache_data:
            return None
        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data.get(key)
