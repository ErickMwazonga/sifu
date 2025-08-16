'''
370. Range Addition
- https://algo.monster/liteproblems/370
- https://leetcode.ca/2016-12-04-370-Range-Addition/

Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments
each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:
Input: length = 5,  updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
Output: [-2, 0, 3, 5, 3]

Explanation:
Initial state: [0, 0, 0, 0, 0]
After applying operation [1, 3, 2]: [0, 2, 2, 2, 0]
After applying operation [2, 4, 3]: [0, 2, 5, 5, 3]
After applying operation [0, 2, -2]: [-2, 0, 3, 5, 3]
'''

from itertools import accumulate

def getModifiedArray(length, updates):
    '''Time: O(n + k), Space: O(n)'''
    
    # difference array
    diff = [0] * length

    # apply updates to difference array
    for start, end, inc in updates:
        diff[start] += inc 
        if end + 1 < length:
            diff[end + 1] -= inc

    # Compute final array with running sum
    result = [0] * length
    result[0] = diff[0]
    for i in range(1, length):
        result[i] = result[i-1] + diff[i]

    return result


def getModifiedArrayV2(length: int,  updates: list[list[int]]) -> list[int]:
    prefix = [0] * length
    for l,  r,  c in updates:
        prefix[l] += c
        if r + 1 < length:
            prefix[r + 1] -= c
            
    return list(accumulate(prefix))