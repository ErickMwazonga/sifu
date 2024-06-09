'''
441. Arranging Coins
Link: https://leetcode.com/problems/arranging-coins/description/

You have n coins and you want to build a staircase with these coins. 
The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
'''


def arrangeCoins(n: int) -> int:
    '''Time: O(n)'''

    i = 0
    while n >= 0:
        i += 1
        n -= i

    return i - 1

def arrangeCoins_v2(n: int) -> int:
    '''Time: O(logn)'''

    low, high = 1, n

    while low <= high:
        mid = (low + high) // 2
        val = (mid * (mid + 1)) // 2

        if val <= n:
            low = mid + 1
        else:
            high = mid - 1

    return high

def arrangeCoins_v3(n: int) -> int:
    '''Time: O(logn)'''

    low, high = 1, n
    res = 0

    while low <= high:
        mid = (low + high) // 2
        val = (mid * (mid + 1)) // 2

        if val > n:
            high = mid - 1
        else:
            low = mid + 1
            res = max(mid, res)
            
    return res