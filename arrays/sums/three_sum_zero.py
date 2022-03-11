'''
15. 3Sum -> 0
Link: https://leetcode.com/problems/3sum/

Are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


def threeSum(nums):
    nums.sort()
    n = len(nums)
    result = set()

    for i in range(n-2):
        low = i + 1
        high = n - 1

        while low < high:
            s = nums[i] + nums[low] + nums[high]

            if s == 0:
                result.add((nums[i], nums[low], nums[high]))
                low += 1
                high -= 1
            if s < 0:
                low += 1
            if s > 0:
                high -= 1

    return result


a = [-1, 0, 1, 2, -1, -4]

print(threeSum(a))
