'''
1764. Form Array by Concatenating Subarrays of Another Array
https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

You are given a 2D integer array groups of length n. You are also given an integer array nums.
You are asked if you can choose n disjoint subarrays from the array nums
such that the ith subarray is equal to groups[i] (0-indexed), and if i > 0,
the (i-1)th subarray appears before the ith subarray in nums (i.e. the subarrays must be in the same order as groups).

Return true if you can do this task, and false otherwise.
Note that the subarrays are disjoint if and only if there is no index k such that nums[k] belongs to more than one subarray.
A subarray is a contiguous sequence of elements within an array.

Example 1:
Input: groups = [[1,-1,-1], [3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]
Output: true
Explanation: You can choose the 0th subarray as [1,-1,0,1,-1,-1,3,-2,0] and the 1st one as [1,-1,0,1,-1,-1,3,-2,0].
These subarrays are disjoint as they share no common nums[k] element.

Example 2:
Input: groups = [[10,-2], [1,2,3,4]], nums = [1,2,3,4,10,-2]
Output: false
Explanation: Note that choosing the subarrays [1,2,3,4,10,-2] and [1,2,3,4,10,-2] is incorrect because they are not in the same order as in groups.
[10,-2] must come before [1,2,3,4].
'''


class Solution:
    def canChoose(self, groups, nums) -> bool:
        pos = 0

        for group in groups:
            text, pattern = nums, group
            pos = self.substring(text, pattern, pos)

            if pos == -1:
                return False

            pos += len(group)

        return True

    # start: starting position of the next substring to check(they have to be in the same order)
    def substring(self, text, pattern, start):
        lps = self.build_lps(pattern)
        i, j = start, 0

        while i < len(text):
            if text[i] == pattern[j]:
                i, j = i + 1, j + 1

                if j == len(pattern):
                    return i - j
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]

        return -1

    def build_lps(self, pattern):
        lps = [0] * len(pattern)  # first lps val will always be one
        prev_lps, i = 0, 1

        while i < len(pattern):
            if pattern[i] == pattern[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps, i = prev_lps + 1, i + 1
            else:
                if prev_lps == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prev_lps = lps[prev_lps - 1]

        return lps
