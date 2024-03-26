'''
16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/

Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1, 2, 1, -4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0, 0, 0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''


def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    N, res = len(nums), float('inf')

    for i in range(N):
        left, right = i + 1, N - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            if abs(curr_sum - target) < abs(res - target):
                res = curr_sum

            if curr_sum == target:
                return curr_sum
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

    return res

def threeSumClosest_v2(nums: list[int], target: int) -> int:
    nums.sort()
    smallest = [float('inf'), float('inf')] # diff, sum

    for i, num in enumerate(nums):
        left, right = i + 1, len(nums) - 1

        while left < right:
            curr_sum = num + nums[left] + nums[right]

            diff = abs(target - curr_sum)
            if diff < smallest[0]:
                smallest = [diff, curr_sum]

            if curr_sum == target:
                return curr_sum
            elif curr_sum > target:
                right -= 1
            else:
                left += 1

    return smallest[1]
