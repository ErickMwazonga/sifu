'''
1980. Find Unique Binary String
https://leetcode.com/problems/find-unique-binary-string/
Credit: https://leetcode.com/problems/find-unique-binary-string/discuss/1418687/Detailed-Explanation-O(N)-Java-C%2B%2B-Python-short-concise-code-Cantor's-Diagonalization

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

    for i, num in enumerate(nums):
        # ans += '1' if num[i] == '0' else '0'
        if num[i] == '0':
            ans += '1'
        else:
            ans += '0'

    return ans
