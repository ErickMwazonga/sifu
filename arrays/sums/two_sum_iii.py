'''
170. Two Sum III - Data structure design
Links: 
1. https://algo.monster/liteproblems/170
2. https://leetcode.com/problems/two-sum-iii-data-structure-design/

Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:
1. TwoSum() Initializes the TwoSum object, with an empty array initially.
2. void add(int number) Adds number to the data structure.
3. boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.

Example 1:
Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false
'''

from collections import Counter

class TwoSum:
    '''
    add Method: Time Complexity: O(1), Space Complexity: O(n) 
    find Method: Time Complexity: O(n), Space Complexity: O(1)
    '''
    
    def __init__(self) -> None:
        # self.num_counter = {}
        self.num_counter = Counter()

    def add(self, number: int) -> None:
        # self.num_counter[number] = self.num_counter.get(number, 0) + 1
        self.num_counter[number] += 1

    def find(self, value: int) -> bool:
        for num, count in self.num_counter.items():
            complement = value - num

            if complement in self.num_counter:
                # If the number and complement are the same, ensure there are at least two occurrences
                if num != complement or count > 1:
                    return True
    
        return False
