'''
278. First Bad Version
Problem Link: https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4

Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
'''


def is_bad_version(n):
    pass


def first_bad_version(n):
    low, high = 0, n

    while low < high:
        mid = low + (high - low) // 2

        if is_bad_version(mid):
            high = mid
        else:
            low = mid + 1

    return low


def first_bad_version2(n):
    low, high = 0, n
    bad = 1

    while low < high:
        mid = low + (high - low) // 2

        if is_bad_version(mid):
            high = mid
            bad = mid
        else:
            low = mid + 1
            bad = low

    return bad
