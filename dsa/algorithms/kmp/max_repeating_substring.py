'''
1668. Maximum Repeating Substring
Link: https://leetcode.com/problems/maximum-repeating-substring/
Resource: https://bit.ly/3zxOBzP

For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence.
The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence.
If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.

Example 1:
Input: sequence = 'ababc', word = 'ab'
Output: 2
Explanation: 'abab' is a substring in 'ababc'.

Example 2:
Input: sequence = 'ababc', word = 'ba'
Output: 1
Explanation: 'ba' is a substring in 'ababc'. 'baba' is not a substring in 'ababc'.
'''


class Solution:
    def maxRepeating(self, sequence, word):
        maxCount_prefix = self.find_max_substring(word, sequence)
        maxCount_suffix = self.find_max_substring(word[::-1], sequence[::-1])

        return max(maxCount_prefix, maxCount_suffix)

    def find_max_substring(self, pattern, text):
        lps = self.get_lps(pattern)
        curr_substring, longest_substring = 0, 0

        i, j = 0, 0
        while i < len(text):
            if text[i] == pattern[j]:
                i, j = i + 1, j + 1

                if j == len(pattern):
                    curr_substring += 1
                    longest_substring = max(curr_substring, longest_substring)
                    j = 0  # check again
            else:
                curr_substring = 0

                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]

        return longest_substring

    def get_lps(self, pattern):
        lps = [0] * len(pattern)
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
