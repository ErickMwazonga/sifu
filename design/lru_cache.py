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


class LRUCache_V2:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            self.dict.move_to_end(key)
        else:
            if self.size < self.capacity:
                self.dict[key] = value
                self.size += 1
            else:
                self.dict.popitem(False)
                self.dict[key] = value
