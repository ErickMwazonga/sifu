'''
146. LRU Cache
https://leetcode.com/problems/lru-cache/
Credit: https://www.youtube.com/watch?v=7ABFKPK2hD4

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

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prev

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        '''
        1. Check if key exists in cache
        2. Get node in cache(hashmap), given the key
        3. It needs to be the most recently used now 
            a. Remove it 
            b. Insert it again
        '''

        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        '''
        1. Check if key exists in cache
            a. Remove it 
            b. Insert it again
        2. Else:
            a. Create a new node and it in cache
            b. Insert it in dll
        3. Check if the cache is full
            a. Remove the least used node from dll
            b. Remoe from cache
        '''

        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)

        if len(self.cache) > self.capacity:
            evicted = self.left.next
            self.remove(evicted)
            self.cache.pop(evicted.key)  # del self.cache[evicted.key]
