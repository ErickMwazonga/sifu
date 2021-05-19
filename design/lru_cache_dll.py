'''
146. LRU Cache
https://leetcode.com/problems/lru-cache/
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
'''


class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left

    def add_node(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prev

    def remove_node(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove_node(node)
        self.add_node(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)

        node = Node(key, value)
        self.add_node(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove_node(lru)
            self.cache.pop(lru.key)
