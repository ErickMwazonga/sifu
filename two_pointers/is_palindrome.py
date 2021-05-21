'''
https://leetcode.com/problems/valid-palindrome/
125. Valid Palindrome
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

"A man, a plan, a canal: Panama" -> true
"race a car" -> false
'''


def isPalindrome(self, s: str) -> bool:
    '''Time complexity: O(N), Space complexity: O(N)'''

    s = s.lower()
    left = ''

    for i in range(0, len(s)):
        if s[i].isalnum():
            left += s[i]

    return left == left[::-1]


def is_palindrome2(s):
    '''Time complexity: O(N), Space complexity: O(1)'''

    s = [i.lower() for i in s if i.isalnum()]
    low, high = 0, len(s) - 1

    while low < high:
        if s[low] != s[high]:
            return False

        low += 1
        high -= 1

    return True


assert isPalindrome('pap') == True
