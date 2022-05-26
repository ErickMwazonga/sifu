'''
316. Remove Duplicate Letters
Link: https://leetcode.com/problems/remove-duplicate-letters/
Similar: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
Credit: https://www.youtube.com/watch?v=2ayws5Y-WM4, https://www.youtube.com/watch?v=j313ttNJjo0

Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Examples:
1. 'bcabc' -> 'abc'
2. 'cbacdcbc' -> 'acdb'
'''

from collections import Counter


def removeDuplicateLetters(s: str) -> str:
    stack, seen = [], set()
    last_occurrence = {char: i for i, char in enumerate(s)}

    for i, char in enumerate(s):
        if char in seen:
            continue

        while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
            popped = stack.pop()
            seen.remove(popped)

        seen.add(char)
        stack.append(char)

    return ''.join(stack)


def removeDuplicateLetters_v2(self, s):
    countMap = Counter(s)
    stack, visited = [], set()

    for ch in s:
        countMap[ch] -= 1

        if ch in visited:
            continue

        while stack and countMap[stack[-1]] > 0 and stack[-1] > ch:
            popped = stack.pop()
            visited.remove(popped)

        stack.append(ch)
        visited.add(ch)

    return ''.join(stack)
