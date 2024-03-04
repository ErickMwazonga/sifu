'''
15. 3Sum -> 0
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


def three_sum_v1(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n, res, target = len(nums), set(), 0

    for i in range(n):
        low, high = i + 1, n - 1
        rem_target = target - nums[i]

        while low < high:
            curr_sum = nums[low] + nums[high]

            if curr_sum == rem_target:
                # list cannot be a set elem coz it's mutable -> TypeError: unhashable type: 'list'
                res.add((nums[i], nums[low], nums[high]))
                low, high = low + 1, high - 1
            elif curr_sum < rem_target:
                low += 1
            else:
                high -= 1

    return list(map(list, res))

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
