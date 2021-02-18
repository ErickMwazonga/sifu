from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        self.lru = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.lru:
            return -1

        v = self.lru.pop(key)
        self.lru[key] = v
        return v

    def put(self, key, value):
        if key in self.lru:
            self.lru.pop(key)
        elif len(self.lru) >= self.capacity:
            self.lru.popitem(last=False)

        self.lru[key] = value
