'''
Non-decreasing Array
https://leetcode.com/problems/non-decreasing-array/

Given an array nums with n integers, your task is to check if it
could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1]
olds for every i (0-based) such that (0 <= i <= n - 2).

Examples:
nums = [4,2,3] -> true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

nums = [4,2,1] -> false
Explanation: You can't get a non-decreasing array by modify at most one element.
'''

def checkPossibility(self, nums):
    count = 0

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            count += 1
            
            if i == 0:
                nums[i] = nums[i + 1]
            elif nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i - 1]
            else:
                nums[i + 1] = nums[i]

        if count > 1:
            return False

    return True


def checkPossibility(self, nums):
    """
    First, find a pair where the order is wrong. Then there are two possibilities,
    either the first in the pair can be modified or the second can be modified to create a valid sequence.
    We simply modify both of them and check for validity of the modified arrays by comparing with the array after sorting.
    """
    one, two = nums[:], nums[:]
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            one[i] = nums[i + 1]
            two[i + 1] = nums[i]
            break

    return one == sorted(one) or two == sorted(two)

    
def checkPossibilityBest(self, nums: List[int]) -> bool:
    count = 0
    n = len(nums)

    if n <= 2:
        return True

    for i in range(0, len(nums)-1):
        if nums[i] > nums[i+1]:
            count += 1

            if count > 1:
                return False
            elif (i-1) >= 0 and nums[i+1] < nums[i-1]:
                nums[i+1] = nums[i]
    return True


def checkPossibility(self, nums: List[int]) -> bool:
    '''
    Explanation:
    Case 1: When size of the input array is 2
    Arrays can be either [0, 0], [1, 2], [5, 3] etc.
    Hence just by adjusting 3the 1st element we can fix the array

    Case 2: When array size is greater than 2
    We count for invalidations ie an element at i-th position is greater than the next element
    Eg. [1, 2, 10, 3, 4, 9, 5] - two elements 10 and 9 are out or order,
    so we bail out once we reach count as 2

    Eg. [1, 2, 3, 4, 1, 2, 3]
    only one element seemingly looks out of order ie 4.
    However, even if we change it, we can't fix the array since the
    element before 4 is greater than the next element.

    Eg. [1, 2, 3, 4, 2, 2, 2]
    since 4 is less than i+2th element and 3 is less than i+1th element,
    even though the count would be 1, we can't fix the array by changing 1 element.
    '''

    count = 0
    i, n = 0, len(nums)

    if n <= 2:
        return True

    while i <= n-2:
        if nums[i] > nums[i+1]:
            count = count + 1

        if count > 1:
            return False

        if (i-1) >= 0 and (i+2) < len(nums):
            if (nums[i] > nums[i+2]) and (nums[i-1] > nums[i+1]):
                return False

        i = i + 1
    return True
