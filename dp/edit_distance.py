'''
72. Edit Distance
https://leetcode.com/problems/edit-distance/

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character
 
Example 1:
Input: word1 = 'horse', word2 = 'ros'
Output: 3
Explanation: 
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')
'''


def min_distance(word1, word2):
    '''Time: O(nm), Space: O(nm)'''

    n, m = len(word1), len(word2)
    dp = [[0] * (m+1) for i in range(n+1)]

    # first row
    for j in range(m+1):
        dp[0][j] = j

    # first col
    for i in range(n+1):
        dp[i][0] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],  # remove
                    dp[i][j-1],  # Insert
                    dp[i-1][j-1]  # replace
                )

    return dp[n][m]
