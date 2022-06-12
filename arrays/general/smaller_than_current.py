'''
1365. How Many Numbers Are Smaller Than the Current Number
Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
Credit: https://bit.ly/39Oory9

Given the array nums, for each nums[i] find out 
how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number 
of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:
Input: nums = [8, 1, 2, 2, 3]
Output: [4, 0, 1, 1, 3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
'''


def smaller_numbers_than_current(nums):
    '''Time: O(nlogn)'''

    sorted_nums = sorted(nums)
    mappings = {}

    for k, v in enumerate(sorted_nums):
        if v not in mappings:
            mappings[v] = k

    return [mappings[x] for x in nums]


nums, res = [8, 1, 2, 2, 3], [4, 0, 1, 1, 3]
assert smaller_numbers_than_current(nums) == res


def smaller_numbers_than_current_v2(nums):
    count = [0] * 102

    for num in nums:
        count[num + 1] += 1

    for i in range(1, 102):
        count[i] += count[i-1]

    return [count[num] for num in nums]


nums, res = [8, 1, 2, 2, 3], [4, 0, 1, 1, 3]
assert smaller_numbers_than_current(nums) == res
