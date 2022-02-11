'''
91. Decode Ways
https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: s = '12' -> 2
    Explanation: It could be decoded as 'AB' (1 2) or 'L' (12).

Example 2:
Input: s = '226' -> 3
    Explanation: It could be decoded as 'BZ' (2 26), 'VF' (22 6), or 'BBF' (2 2 6).
'''


def num_decodings(s: str) -> int:
    if not s:
        return 0

    n = len(s)
    dp = [0] * (n + 1)

    # base case initialization
    dp[0] = 1
    dp[1] = 0 if s[0] == '0' else 1

    for i in range(2, n + 1):
        # One step jump
        if 0 < int(s[i-1:i]) <= 9:
            dp[i] += dp[i - 1]

        # Two step jump
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i - 2]

    return dp[n]


# RECURSION
def ways_to_decode(str, i=0):
    '''Time complexity: O(2^n), Space complexity: O(n)'''

    n = len(str)
    if n == 0 or (i < n and str[i] == '0'):
        return 0
    elif i >= n-1:
        return 1
    elif '10' <= (str[i] + str[i+1]) <= '26':
        return ways_to_decode(str, i+1) + ways_to_decode(str, i+2)
    else:
        return ways_to_decode(str, i+1)
