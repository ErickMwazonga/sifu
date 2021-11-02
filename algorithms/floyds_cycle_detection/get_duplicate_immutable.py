'''
https://leetcode.com/problems/find-the-duplicate-number/

https://www.youtube.com/watch?v=dfIqLxAf-8s
https://leetcode.com/problems/find-the-duplicate-number/discuss/705111/summary-7-solutions-%2B-consice-explanation-and-complexity-analysis
'''


def findDuplicate(nums) -> int:
    slow = nums[0]
    fast = nums[slow]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow = nums[0]
    while slow != fast:
        slow, fast = nums[slow], nums[fast]

    return slow
