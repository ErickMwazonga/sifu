'''
Longest Prefix Suffix 
Resources: [
    https://iq.opengenus.org/prefix-table-lps/,
    https://www.youtube.com/watch?v=V5-7GzOfADQ&t=75s,
    https://www.youtube.com/watch?v=GTJr8OvyEVQ,
    https://www.youtube.com/watch?v=BXCEFAzhxGY
]

This problem is part of GFG SDE Sheet. Click here to view more.   
Given a string of characters, find the length of the longest proper prefix which is also a proper suffix.

NOTE: Prefix and suffix can be overlapping but they should not be equal to the entire string.

Examples:
1. 'abab' -> 2
    Explanation: 'ab' is the longest proper prefix and suffix. 
2. 'aaaa' -> 3
    Explanation: 'aaa' is the longest proper prefix and suffix. 
'''


class Solution:
    def longest_lps(self, pattern):
        lps = self.build_lps(pattern)
        return lps[-1]

    def build_lps(pattern):
        lps = [0] * len(pattern)  # first lps val will always be one
        prev_lps, i = 0, 1

        while i < len(pattern):
            if pattern[i] == pattern[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps, i = prev_lps + 1, i + 1
            else:
                if prev_lps == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prev_lps = lps[prev_lps - 1]

        return lps
