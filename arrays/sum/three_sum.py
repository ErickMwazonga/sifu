"""
Find a triplet that sum to a given value
Given an array and a value, find if there is a triplet in array
whose sum is equal to the given value.
If there is such a triplet present in array, then print the triplet
and return true. Else return false.

For example,
if the given array is {12, 3, 4, 1, 6, 9} and given sum is 24,
then there is a triplet (12, 3 and 9) present in array whose sum is 24.
"""


def three_sum(nums, target):
    '''Time complexity: 0(n^2)'''

    nums.sort()

    for i in range(len(nums)-2):
        partial_target = target - nums[i]
        j = i + 1
        k = len(nums) - 1

        while j < k:
            partial_sum = nums[j] + nums[k]
            if partial_sum == partial_target:
                print([nums[i], nums[j], nums[k]])
                return True
            elif partial_sum > partial_target:
                k -= 1
            else:
                j += 1
    return False


assert three_sum([12, 3, 4, 1, 6, 9], 24) == True
assert three_sum([12, 3, 4, 1, 6, 9], 28) == False
