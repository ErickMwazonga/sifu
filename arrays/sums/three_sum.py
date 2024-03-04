'''
Find a triplet that sum to a given value

Given an array and a value, find if there is a triplet in array
whose sum is equal to the given value.
If there is such a triplet present in array, then print the triplet
and return true. Else return false.

For example,
if the given array is [12, 3, 4, 1, 6, 9] and given sum is 24,
then there is a triplet [12, 3 and 9] present in array whose sum is 24.
'''

class Solution:

    def three_sum(self, nums: list[int], target: int) -> bool:
        '''Time: 0(n^2)'''

        nums.sort()
        n = len(nums)

        for i in range(n):
            rem_target = target - nums[i]
            if self.two_sum(nums, i + 1, n - 1, rem_target):
                return True

        return False
    
    def two_sum(self, nums: list[int], left: int, right: int, target: int) -> bool:
        while left < right:
            curr_sum = nums[left] + nums[right]

            if curr_sum == target:
                return True
            elif curr_sum > target:
                right -= 1
            else:
                left += 1

        return False


soln = Solution()
assert soln.three_sum([12, 3, 4, 1, 6, 9], 24) == True
assert soln.three_sum([12, 3, 4, 1, 6, 9], 28) == False
