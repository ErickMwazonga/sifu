'''
259 - 3Sum Smaller

Given an array of n integers nums and an integer target, 
find the number of index triplets i, j, k with 0 <= i < j < k < n 
that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example 1:
Input: nums = [-2, 0, 1, 3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2, 0, 1]
[-2, 0, 3]

Example 2:
Input: nums = [], target = 0
Output: 0

Example 3:
Input: nums = [0], target = 0
Output: 0
'''


def threeSumSmaller(nums: list[int], target: int) -> int:
    nums.sort()
    ans, N = 0, len(nums)

    for i in range(N):
        left, right = i + 1, N - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum < target:
                # If the sum is smaller than target, all elements between left and right
                # form valid triplets with nums[i] because the array is sorted
                ans += right - left
                left += 1
            else:
                right -= 1
    return ans


assert len(threeSumSmaller([-2, 0, 1, 3], 2)) == 2
assert len(threeSumSmaller([], 0)) == 0
assert len(threeSumSmaller([0], 0)) == 0