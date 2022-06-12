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
    n, res = len(nums), set()

    for i in range(n):
        low, high = i + 1, n - 1
        target = 0 - nums[i]

        while low < high:
            _sum = nums[low] + nums[high]

            if _sum == target:
                res.add((nums[i], nums[low], nums[high]))
                low, high = low + 1, high - 1
            elif _sum < target:
                low += 1
            else:
                high -= 1

    return res


a = [-1, 0, 1, 2, -1, -4]

print(threeSum(a))
