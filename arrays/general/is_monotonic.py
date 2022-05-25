'''
896. Monotonic Array
Link: https://leetcode.com/problems/monotonic-array/

An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Examples:
1. [1, 2, 2, 3] -> True
2. [6, 5, 4, 4] -> True
3. [1, 3, 2] -> False
'''


def isMonotonic(nums) -> bool:
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)


def isMonotonic_v2(A) -> bool:
    increasing = all([A[i] >= A[i-1] for i in range(1, len(A))])
    decreasing = all([A[i] <= A[i-1] for i in range(1, len(A))])

    return increasing or decreasing


def isMonotonic_v3(A):
    def mono_inc(A):
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return False

        return True

    def mono_dec(A):
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                return False

        return True

    return mono_inc(A) or mono_dec(A)


assert isMonotonic_v3([1, 2, 2, 3]) == True
assert isMonotonic_v3([6, 5, 4, 4]) == True
assert isMonotonic_v3([1, 3, 2]) == False
