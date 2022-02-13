'''
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/

Given a non-empty string s, you may delete at most one character.
Judge whether you can make it a palindrome.

Examples:
1. 'aba' -> True
2. 'abca' -> True [Explanation: You could delete the character 'c'].
'''


def validPalindrome(s: str) -> bool:
    left, right = 0, len(s)

    while left < right:
        if s[left] == s[right]:
            # Move inwards
            left += 1
            right -= 1
        else:
            # Get the subsets eliminating either of the chars
            first, second = s[left+1: right+1], s[left: right]
            return first == first[::-1] or second == second[::-1]


assert validPalindrome('aba') == True
assert validPalindrome('abca') == True
