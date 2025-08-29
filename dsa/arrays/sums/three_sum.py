'''
Find a triplet that sum to a given value

Given an array and a value, find if there is a triplet in array
whose sum is equal to the given target.
If there is such a triplet present in array, then print the triplet otherwise return -1.

For example,
if the given array is [12, 3, 4, 1, 6, 9] and given sum is 24,
then there is a triplet [12, 3 and 9] present in array whose sum is 24.
'''

from typing import List, Optional

class Solution:

    def three_sum(self, nums: list[int], target: int) -> Optional[List[int]]:
        '''Time: 0(n^2)'''

        nums.sort()
        n = len(nums)

        for i, num in enumerate(nums):
            rem_target = target - nums[i]
            two_sum_candidates = self.two_sum(nums, i + 1, n - 1, rem_target)
            if two_sum_candidates:
                return [num] + two_sum_candidates

        return None
    
    def two_sum(self, nums: list[int], left: int, right: int, target: int) -> Optional[List[int]]:
        while left < right:
            curr_sum = nums[left] + nums[right]

            if curr_sum == target:
                return [nums[left], nums[right]]
            elif curr_sum > target:
                right -= 1
            else:
                left += 1

        return None


soln = Solution()
assert soln.three_sum([12, 3, 4, 1, 6, 9], 24) == True
assert soln.three_sum([12, 3, 4, 1, 6, 9], 28) == False
