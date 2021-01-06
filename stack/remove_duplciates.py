'''
316. Remove Duplicate Letters
https://leetcode.com/problems/remove-duplicate-letters/
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
https://www.youtube.com/watch?v=2ayws5Y-WM4

Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Examples:
Input: s = "bcabc"
Output: "abc"

Input: s = "cbacdcbc"
Output: "acdb"
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurrence = {}
        
        # last_occurrence = {char: i for i, char in enumerate(s)}
        
        for i, char in enumerate(s):
            last_occurrence[char] = i
            
        for i, char in enumerate(s):
            if char in seen:
                continue
            else:
                while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                    removed_char = stack.pop()
                    seen.remove(removed_char)
            
            seen.add(char)
            stack.append(char)
        
        return ''.join(stack)