#!/usr/bin/env python3
'''
Caching that uses the Least Frequently Used mechanism
'''
from collections import OrderedDict, defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''Most Recently Used eviction mechanism in caching'''
    def __init__(self):
        '''init/constructor method'''
        super().__init__()
        self.frequency = defaultdict(int)
        self.lru_order = []

    def put(self, key, item):
        '''Add an item by key'''
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.frequency[key] += 1

        if key in self.lru_order:
            self.lru_order.remove(key)
        self.lru_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_frequent = min(self.frequency.values())
            least_frequent_keys = [k for k, v in self.frequency.items()
                                   if v == least_frequent]

            if len(least_frequent_keys) == 1:
                evicted_key = least_frequent_keys[0]
            else:
                evicted_key = self.lru_order.pop(0)

            del self.cache_data[evicted_key]
            del self.frequency[evicted_key]
            print(f"DISCARD: {evicted_key}")

    def get(self, key):
        '''Get an item key'''
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data.get(key)
