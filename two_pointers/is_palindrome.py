'''
125. Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Examples
1. 'A man, a plan, a canal: Panama' -> true
2. 'race a car' -> false
'''


def is_palindrome(s):
    '''Time: O(N), Space: O(1)'''

    s = [i.lower() for i in s if i.isalnum()]
    low, high = 0, len(s) - 1

    while low < high:
        if s[low] != s[high]:
            return False

        low += 1
        high -= 1

    return True


assert is_palindrome('pap') == True
assert is_palindrome('race a car') == False
assert is_palindrome('A man, a plan, a canal: Panama') == True
