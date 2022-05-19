'''
496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/
Resource: https://www.youtube.com/watch?v=68a1Dc_qVq4

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:
Input: nums1 = [4, 1, 2],  nums2 = [1, 3, 4, 2]
Output: [-1, 3, -1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1, 3, 4, 2]. There is no next greater element,  so the answer is -1.
- 1 is underlined in nums2 = [1, 3, 4, 2]. The next greater element is 3.
- 2 is underlined in nums2 = [1, 3, 4, 2]. There is no next greater element, so the answer is -1.
'''

# MONOTONIC STACK


def nextGreaterElement(nums1, nums2):
    '''Time: O(N*M), Space: O(N)'''

    n, m = len(nums1), len(nums2)

    nums1_idx = {n: i for i, n in enumerate(nums1)}
    res = [-1] * n

    for i in range(m):
        if nums2[i] not in nums1_idx:
            continue

        for j in range(i + 1, m):
            if nums2[j] > nums2[i]:
                curr_num = nums2[i]
                idx = nums1_idx[curr_num]
                res[idx] = nums2[j]
                break

    return res


def nextGreaterElement_v2(nums1, nums2):
    '''Time: O(N + M), Space: O(N)'''

    n, m = len(nums1), len(nums2)

    nums1_idx = {n: i for i, n in enumerate(nums1)}
    res = [-1] * n

    stack = []
    for i in range(m):
        curr = nums2[i]

        while stack and curr > stack[-1]:
            val = stack.pop()
            idx = nums1_idx[val]
            res[idx] = curr

        if curr in nums1_idx:
            stack.append(curr)

    return res
