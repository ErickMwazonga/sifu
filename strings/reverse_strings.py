'''
344. Reverse String
Link: https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Examples:
1. ['h','e','l','l','o'] -> ['o','l','l','e','h']
2. ['H','a','n','n','a','h'] -> ['h','a','n','n','a','H']
'''


def reverseString(s):
    s[:] = s[::-1]
    return s


def reverseString_v2(s):
    s.reverse()


def reverse_v3(chars: list):
    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return chars
