'''
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = 'abcabcbb' -> 3
    Explanation: The answer is 'abc', with the length of 3.
Example 2:
    Input: s = 'bbbbb' -> 1
    Explanation: The answer is 'b', with the length of 1.
Example 3:
    Input: s = 'pwwkew' -> 3
    Explanation: The answer is 'wke', with the length of 3.
    Notice that the answer must be a substring, 'pwke' is a subsequence and not a substring.
Example 4:
    Input: s = ''
    Output: 0
'''


def lengthOfLongestSubstring(s):
    '''Time:  O(n), Space: O(k) - [k = length of the longest substring w/o repeating characters]'''

    n = len(s)
    longest = left = right = 0
    seen = set()

    while left < n and right < n:
        if s[right] in seen:
            seen.remove(s[left])
            left += 1
        else:
            seen.add(s[right])
            right += 1
            longest = max(longest, right - left)

    return longest


def longestSubstring(s):
    start = max_length = 0
    seen_chars = {}

    for i, c in enumerate(s):
        # seen_chars[c] >= start: we do not want to count chars before the start
        if c in seen_chars and seen_chars[c] >= start:
            start = seen_chars[c] + 1
        else:
            max_length = max(max_length, i - start + 1)

        seen_chars[c] = i

    return max_length


assert lengthOfLongestSubstring('abcabcbb') == 3
assert lengthOfLongestSubstring('bbbbb') == 1
assert lengthOfLongestSubstring('pwwkew') == 3
assert lengthOfLongestSubstring('') == 0
