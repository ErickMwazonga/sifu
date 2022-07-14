'''
1374. Generate a String With Characters That Have Odd Counts
https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.
The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  

Examples
1. 4 -> 'pppz'
    Explanation: 'pppz' is a valid string since the character 'p' occurs three times and the character 'z' occurs once. 
    Note that there are many other valid strings such as 'ohhh' and 'love'.

2. 2 -> 'xy'
    Explanation: 'xy' is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as 'ag' and 'ur'.

3. 7 -> 'holasss'
'''

def generateTheString(n: int) -> str:
    ans = ''

    if n % 2 != 0:
        ans += 'a' * n
    else:
        ans += 'a' * (n - 1)
        ans += 'b'

    return ans

def generateTheString_v2(n: int) -> str:
    is_odd = n % 2
    
    if is_odd:
        return 'a' * n
    else:
        return 'a' * (n-1) + 'b' * 1