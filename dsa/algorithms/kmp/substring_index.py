'''
Get substring index

Given two strings str1 and str2, create a function that returns the first index where we can find str2 in str1.
If we cannot find str2 in str1, the function must return -1.
Try to solve the problem without using the built-in .indexOf() method.

Example 1:
Input: str1 = 'inside', str2 = 'side'
Output: 2
Explanation: we can find 'side' in 'inside' by starting from the index 2

Example 2:
Input: str1 = 'inside', str2 = 'in'
Output: 0
Explanation: we can find 'in' in 'inside' by starting from the index 0

Example 3:
Input: str1 = 'inside', str2 = 'code'
Output: -1
Explanation: we can't find 'code' in 'inside'
'''


def substrIndex(str1, str2):
    n, m = len(str1), len(str2)

    if not str1 or not str2:
        return -1

    if m > n:
        return -1

    if str2[0] not in str1:
        return -1

    i, j = 0, 0
    while i < n and j < m:
        if str1[i] != str2[j]:
            i += 1
        else:
            k = i

            while k < n and str1[k] == str2[j]:
                k, j = k + 1, j + 1

                if k - i == m:
                    return i

            j = 0
            i += 1

    return -1
