'''
1980. Find Unique Binary String
Link: https://leetcode.com/problems/find-unique-binary-string/
Credit: https://bit.ly/3PvueJj

Given an array of strings nums containing n unique binary strings each of length n, 
return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:
1. ['01', '10'] -> '11'
Explanation: '11' does not appear in nums. '00' would also be correct.

2. ['111', '011', '001'] -> '101'
Explanation: '101' does not appear in nums. '000', '010', '100', and '110' would also be correct.
'''


def findDifferentBinaryString(nums) -> str:
    ans = ''

    for i, group in enumerate(nums):
        ans += '1' if group[i] == '0' else '0'

    return ans
