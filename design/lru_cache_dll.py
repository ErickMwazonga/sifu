class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_node(self, node):
        tail = self.tail.prev
        tail.next = node
        self.tail.prev = node
        node.prev = tail
        node.next = self.tail
        
    def remove_node(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        
        node = self.lru[key]
        self.remove_node(node)
        self.add_node(node)
        
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node_to_remove = self.lru[key]
            self.remove_node(node_to_remove)
        
        node = Node(key, value)
        self.add_node(node)
        self.lru[key] = node
        
        if len(self.lru) >= self.capacity:
            nxt = self.head.next
            self.remove_node(nxt)
            self.lru.pop(nxt.key)