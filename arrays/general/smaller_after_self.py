'''
315. Count of Smaller Numbers After Self
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''

import bisect


def count_smaller(nums):
    '''Time Complexity: ~Nlog(N), Space Complexity: ~N'''

    result = []
    sorted_nums = []

    for num in reversed(nums):
        index = bisect.bisect_left(sorted_nums, num)
        sorted_nums.insert(index, num)
        result.insert(0, index)

    return result


assert count_smaller([5, 2, 6, 1]) == [2, 1, 1, 0]
