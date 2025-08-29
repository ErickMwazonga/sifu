'''
503. Next Greater Element II
Link: https://leetcode.com/problems/next-greater-element-ii/
Resource: https://www.youtube.com/watch?v=SfNlyzNEKyg

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array, 
which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:
1. [1, 2, 1] -> [2, -1, 2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
'''


def nextGreaterElements(nums):
    '''Time: O(N*N), Space: O(N)'''

    n = len(nums)
    res = [-1] * n
    new_nums = nums * 2

    for i in range(n):
        for j in range(i+1, len(new_nums)):
            if new_nums[j] > nums[i]:
                res[i] = new_nums[j]
                break

    return res


def nextGreaterElements_v2(nums):
    n = len(nums)

    new_nums = nums + nums
    res = [-1] * n
    stack = []

    for i in range(len(new_nums)):
        num = new_nums[i]

        while stack and num > stack[-1][0]:
            val, pos = stack.pop()
            res[pos] = num  # res[pos % i] = num

        if i < n:
            stack.append((num, i))

    return res


def nextGreaterElements_v3(nums):
    n = len(nums)

    new_nums = nums + nums
    res = [-1] * n
    stack = []

    for i in range(len(new_nums)):
        num = new_nums[i]

        while stack and num > stack[-1][0]:
            val, pos = stack.pop()

            if pos >= n:
                continue

            res[pos] = num

        stack.append((num, i))

    return res
