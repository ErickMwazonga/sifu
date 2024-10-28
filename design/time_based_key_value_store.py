'''
981. Time Based Key-Value Store
Link: https://leetcode.com/problems/time-based-key-value-store/

Design a time-based key-value data structure that can store multiple values 
for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
    1. TimeMap() Initializes the object of the data structure.
    2. void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    3. String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
        If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
'''

from collections import defaultdict


class TimeMap:
    '''
    Time:
        set: O(1) for inserting a [value, timestamp] pair into the list associated with a key in self.dic.
        get: O(log n) for performing binary search on the list of [value, timestamp] pairs.
    Space:
        O(n) for storing all [value, timestamp] pairs in self.store
    '''

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self.store.get(key, [])

        low, high = 0, len(values) - 1
        while low <= high :
            mid = (low + high) // 2
            val, mid_timestamp = values[mid]

            if mid_timestamp <= timestamp:
                low = mid + 1
                res = val
            else:
                high = mid - 1

        return res
        