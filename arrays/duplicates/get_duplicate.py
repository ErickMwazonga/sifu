'''
Find the Duplicate Number

Given an array nums containing n + 1 integers
where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist.
Assume that there is only one duplicate number,
find the duplicate one.
'''

def findDuplicate(nums):
    for v in nums:
        pos = abs(v) - 1

        if nums[pos] < 0:
            return pos + 1

        nums[pos] = -nums[pos]

assert findDuplicate([1,3,4,2,2]) == 2
assert findDuplicate([1,2,4,3,3]) == 3

