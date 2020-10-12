'''
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb" -> 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb" -> 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew" -> 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
'''

def lengthOfLongestSubstring(self, s):
    """
    Time:  O(n)
    Space: O(k)
    [k = length of the longest substring w/o repeating characters]
    """
    longest = 0
    left, right = 0, 0
    seen = set()

    while left < len(s) and right < len(s):
        if s[right] not in seen:
            seen.add(s[right])
            right += 1
            longest = max(longest, right - left)
        else:
            seen.remove(s[left])
            left += 1

    return longest


def longestSubstring(s):
	start = maxLength = 0
    usedChar = {}

    for i, c in enumerate(s):
        if c in usedChar and start <= usedChar[c]:
            start = usedChar[c] + 1
        else:
            maxLength = max(maxLength, i - start + 1)
        
        usedChar[c] = i

    return maxLength
