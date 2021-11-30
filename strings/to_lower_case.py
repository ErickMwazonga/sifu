'''
709. To Lower Case
https://leetcode.com/problems/to-lower-case/
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Input: 'Hello' -> 'hello'
Input: 'here' -> 'here'
Input: 'LOVELY' -> 'lovely'
'''


class Solution:
    def toLowerCase(self, str):
        lowered = []
        for i in str:
            char_code = ord(i)
            # if A-Z
            if char_code < 91 and char_code > 64:
                lowered += chr(char_code + 32)
            else:
                lowered += i
        return ''.join(lowered)

    def toLowerCase2(self, str: str) -> str:
        res = ''

        for i in range(len(str)):
            if(ord(str[i]) >= 65 and ord(str[i]) <= 90):
                res += chr(ord(str[i])+32)
            else:
                res += str[i]
        return res


soln = Solution()
soln.toLowerCase('Hello') == 'hello'
soln.toLowerCase('here') == 'here'
soln.toLowerCase('LOVELY') == 'lovely'
