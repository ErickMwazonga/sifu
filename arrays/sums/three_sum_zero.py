'''
15. 3Sum Zero
Link: https://leetcode.com/problems/3sum/

Are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

Example 2:
Input: nums = [0, 1, 1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0, 0, 0]
Output: [[0, 0, 0]]
'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for i, num in enumerate(nums):
            remaining_target = 0 - num
            left, right = i + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == remaining_target:
                    # a hashset can only have immutable keys 
                    # hence adding tuple not list -> TypeError: unhashable type: 'list'
                    result.add((num, nums[left], nums[right]))
                    left, right = left + 1, right - 1
                elif curr_sum < remaining_target:
                    left += 1
                else:
                    right -= 1

        return [list(triplet) for triplet in result] # list(map(list, res))

class Solution_V2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result, N = set(), len(nums)

        for i, num in enumerate(nums):
            remaining_target = 0 - num
            two_sum_result = self.find_two_sum(nums, remaining_target, i + 1, N - 1)

            three_sum_result = [[num] + two_sum for two_sum in two_sum_result]
            for triplet in three_sum_result:
                result.add(tuple(triplet))

        return [list(triplet) for triplet in result]

    def find_two_sum(self, nums: List[int], target: int, left: int, right: int) -> List:
        result = []
        while left < right:
            current_sum = nums[left] + nums[right]
            # there could be other comninations that add upto the raget
            if current_sum == target: 
                result.append([nums[left], nums[right]])
                left, right = left + 1, right - 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return result


def three_sum_v2(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n, res, target = len(nums), [], 0

    for i in range(n):
        # skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        low, high = i + 1, n - 1
        rem_target = target - nums[i]

        while low < high:
            curr_sum = nums[low] + nums[high]

            if curr_sum == rem_target:
                res.append([nums[i], nums[low], nums[high]])
                while low < high and nums[low] == nums[low + 1]:
                    low += 1
                while low < high and nums[high] == nums[high - 1]:
                    high -= 1
                low, high = low + 1, high - 1
            elif curr_sum < rem_target:
                low += 1
            else:
                high -= 1

    return res

# Sorted = [-4, -1, -1, 0, 1, 2]
print(three_sum_v2([-1, 0, 1, 2, -1, -4]))
