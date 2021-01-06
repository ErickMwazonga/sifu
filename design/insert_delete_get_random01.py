'''
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/

Implement the RandomizedSet class:

Design a data structure that supports all following operations in average O(1) time.
    insert(val): Inserts an item val to the set if not already present.
    remove(val): Removes an item val from the set if present.
    getRandom: Returns a random element from current set of elements
        (it’s guaranteed that at least one element exists when this method is called).
        Each element must have the same probability of being returned.

Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
'''

import random


class RandomizedSet:

    def __init__(self):
        self.values_indexes = {}
        self.values = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        
        if val not in self.values_indexes:
            self.values_indexes[val] = len(self.values)
            self.values.append(val)
            
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        
        if val not in self.values_indexes:
            return False
        else:
            index = self.values_indexes[val]
            last = len(self.values) - 1
            
            self.values_indexes[self.values[last]] = index
            
            self.values[index], self.values[last] = self.values[last], self.values[index]
            self.values.pop()
            
            del self.values_indexes[val]
            
            return True

        def getRandom(self) -> int:
            """
            Get a random element from the set.
            """

            n = len(self.values)
            random_index = random.randint(0, n - 1)        

            return self.values[random_index]

            # return random.choice(self.values)