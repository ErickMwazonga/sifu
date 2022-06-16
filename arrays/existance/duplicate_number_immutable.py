'''
287. Find the Duplicate Number
Link: https://leetcode.com/problems/find-the-duplicate-number/

Resource: https://www.youtube.com/watch?v=dfIqLxAf-8s
Resource: https://bit.ly/3NtUh1I
'''


def find_duplicate(nums) -> int:
    slow = nums[0]
    fast = nums[slow]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow = 0
    while slow != fast:
        slow, fast = nums[slow], nums[fast]

    return slow
