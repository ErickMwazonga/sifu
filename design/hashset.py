'''
705. Design HashSet
https://leetcode.com/problems/design-hashset/description/
Explanation: https://www.youtube.com/watch?v=VymjPQUXjL8

Design a HashSet without using any built-in hash table libraries.
Implement MyHashSet class:

1. void add(key) Inserts the value key into the HashSet.
2. bool contains(key) Returns whether the value key exists in the HashSet or not.
3. void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Example 1:
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
'''

class MyHashSet:
    def __init__(self):
        self.data = set()

    def add(self, key: int) -> None:
        self.data.add(key)

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.data



class ListNode:
    def __init__(self, val: int = -1):
        self.val = val
        self.next = None

class MyHashSet_V2:
    def __init__(self) -> None:
        self.size = 1000
        self.buckets = [ListNode() for _ in range(self.size)]
    
    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> bool:
        if self.contains(key):
            return

        idx = self._hash(key)
        head = self.buckets[idx]

        curr = head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> bool:
        if not self.contains(key):
            return

        idx = self._hash(key)
        head = self.buckets[idx]
        
        curr = head
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> None:
        idx = self._hash(key)
        head = self.buckets[idx]

        curr = head.next
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False