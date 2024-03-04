'''
Check if pair with given Sum exists in Array (Two Sum)

Given an array A[] of n numbers and another number target, 
the task is to check whether or not there exist two elements in A[] whose sum is exactly x. 

Example 1: 
Input: nums = [0, -1, 2, -3, 1], target = -2
Output: True
Explanation:  If we calculate the sum of the output, 1 + (-3) = -2

Example 2:
Input: nums = [1, -2, 1, 0, 5], x = 0
Output: False
'''

def two_sum_v1(nums: list[int], target: int) -> bool:
    '''Time: O(n^2), Space: O(1)'''

    N = len(nums)

    for i in range(N):
        for j in range(i + 1, N):
            if nums[i] + nums[j] == target:
                return True
    return False

def two_sum_v2(nums: list[int], target: int) -> bool:
    '''Time: O(nlogn), Space: O(1)'''

    nums.sort()
    left, right = 0, len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum == target:
            return True
        elif curr_sum > target:
            right -= 1
        else:
            left += 1

    return False


def two_sum_v3(nums: list, target: int) -> bool:
    '''Time: 0(n), Space: 0(n)'''

    seen = {}

    for key, value in enumerate(nums):
        rem = target - value

        if rem in seen:
            return True
        
        seen[value] = key

    return False


assert two_sum_v1([0, -1, 2, -3, 1], -2) == True
assert two_sum_v1([1, -2, 1, 0, 5], 0) == False

