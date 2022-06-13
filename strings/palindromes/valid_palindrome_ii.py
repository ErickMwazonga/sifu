'''
680. Valid Palindrome II
Link: https://leetcode.com/problems/valid-palindrome-ii/

Given a non-empty string s, you may delete at most one character.
Judge whether you can make it a palindrome.

Examples:
1. 'aba' -> True
2. 'abca' -> True [Explanation: You could delete the character 'c'].
'''


def validPalindrome(s):
    if s == s[::-1]:
        return True

    for i in range(len(s)):
        temp = s[:i] + s[i+1:]

        if temp == temp[::-1]:
            return True

    return False


def validPalindrome_v2(s):
    i, j = 0, len(s) - 1

    def is_pali(x): return x == x[::-1]

    while i < j:
        if s[i] == s[j]:
            i, j = i + 1, j - 1
        else:
            exclude_last = s[i:j]
            exclude_first = s[i + 1:j + 1]

            return is_pali(exclude_last) or is_pali(exclude_first)

    return True


def validPalindrome_v3(s: str) -> bool:
    left, right = 0, len(s)

    while left < right:
        if s[left] == s[right]:
            # Move inwards
            left, right = left - 1, right + 1
        else:
            # Get the subsets eliminating either of the chars
            first, second = s[left+1: right+1], s[left: right]
            return first == first[::-1] or second == second[::-1]


assert validPalindrome('aba') == True
assert validPalindrome('abca') == True
