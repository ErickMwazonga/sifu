'''
Longest common substring
Given two strings str1 and str2 made of alphabetical letters only,
create a function that returns the length of their longest common substring.

Example 1:
    Input: str1 = "opposite", str2 = "position"
    Output: 5
    Explanation: the longest common substring of str1 and str2 is "posit"
Example 2:
    Input: str1 = "printer", str2 = "external"
    Output: 3
    Explanation: the longest common substring of str1 and str2 is "ter"
Example 3:
    Input: str1 = "table", str2 = "dog"
    Output: 0
    Explanation: the longest common substring of str1 and str2 is ""
'''

def lcs(str1, str2):
    '''
    Time complexity: O(nm), Space complexity: O(nm)
    '''
    n, m = len(str1), len(str2)
    
    dp = [[0] * (m+1) for i in range(n+1)]
    maxLength = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                maxLength = max(maxLength, dp[i][j])
            else:
                dp[i][j] = 0
    return maxLength