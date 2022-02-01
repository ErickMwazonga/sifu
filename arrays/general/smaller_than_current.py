'''
1365. How Many Numbers Are Smaller Than the Current Number
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/discuss/524865/Clean-Python-3-sorting-and-counting

Given the array nums, for each nums[i] find out 
how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number 
of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
'''


def smallerNumbersThanCurrent(nums):
    '''Time complexity: O(nlogn)'''

    sorted_nums = sorted(nums)
    mappings = {}

    for k, v in enumerate(sorted_nums):
        if v not in mappings:
            mappings[v] = k
    return [mappings[x] for x in nums]


nums = [8, 1, 2, 2, 3]
assert smallerNumbersThanCurrent(nums) == [4, 0, 1, 1, 3]


def smallerNumbersThanCurrent2(nums):
    count = [0] * 102
    for num in nums:
        count[num + 1] += 1

    for i in range(1, 102):
        count[i] += count[i-1]

    return [count[num] for num in nums]


nums = [8, 1, 2, 2, 3]
assert smallerNumbersThanCurrent2(nums) == [4, 0, 1, 1, 3]
