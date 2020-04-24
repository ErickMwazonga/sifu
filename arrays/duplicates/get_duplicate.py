'''
Find the Duplicate Number

Given an array nums containing n + 1 integers
where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist.
Assume that there is only one duplicate number,
find the duplicate one.

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

def findDuplicate(nums):
    '''
    Time complixity 0(n)
    Space Complexity 0(1) extra space
    '''
    for v in nums:
        pos = abs(v) - 1

        if nums[pos] < 0:
            return pos + 1

        nums[pos] = -nums[pos]


def getDuplicate(A): 
    length = len(A) - 1
    total = length * (length + 1) // 2

    sum_of_A = sum(A) 
    return sum_of_A - total


assert findDuplicate([1,3,4,2,2]) == 2
assert findDuplicate([1,2,4,3,3,3]) == 3

# SIngle duplicate
assert getDuplicate([1,3,4,2,2]) == 2
assert getDuplicate([1,2,4,3,3]) == 3
