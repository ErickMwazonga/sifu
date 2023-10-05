'''
28. Implement strStr()
Link: https://leetcode.com/problems/implement-strstr/

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Examples:
Input: haystack = 'hello', needle = 'll'
Output: 2

Input: haystack = 'aaaaa', needle = 'bba'
Output: -1

Input: haystack = '', needle = ''
Output: 0

The Rabin-Karp algorithm or Karp-Rabin algorithm is a string-searching algorithm
created by Richard M. Karp and Michael O. Rabin (1987)
that uses hashing to find an exact match of a pattern string in a text.
It uses a rolling hash to quickly filter out positions of the text that cannot match the pattern,
and then checks for a match at the remaining positions. Generalizations of the same idea can be
used to find more than one match of a single pattern, or to find matches for more than one pattern.

1. https://github.com/mission-peace/interview/blob/master/python/string/rabinkarp.py
2. https://bit.ly/3wLgktM
3. Link: https://leetcode.com/problems/implement-strstr/discuss/1019737/Rabin-karp-algorithm-with-explanation-Python
'''


class Solution:

    def __init__(self):
        self.base = 26  # base of the polynomial hash
        self.prime_mod = 101  # to avoid hash overflow, doesn't have to be prime number
        self.pattern_hash = self.myhash()

    def check_equal(self, str1, str2):
        if len(str1) != len(str2):
            return False

        i = j = 0
        for i, j in zip(str1, str2):
            if i != j:
                return False

        return True

    def create_hash(self, _str, end):
        my_hash = 0

        for i in range(end + 1):
            my_hash = my_hash + (ord(_str[i]) * self.base ** i)

        return my_hash

    def recalculate_hash(self, _str, start, end, old_hash, pattern_len):
        prev_char_code = ord(_str[start]) * self.base ** pattern_len - 1
        new_hash = new_hash - prev_char_code

        new_char_code = ord(_str[end]) * self.base ** 0
        new_hash += new_char_code

        return new_hash

    # def recalculate_hash(self, _str, old_index, new_index, old_hash, pattern_len):
    #     new_hash = old_hash - ord(_str[old_index])
    #     new_hash = new_hash/self.prime
    #     new_hash += ord(_str[new_index]) * pow(self.prime, pattern_len - 1)
    #     return new_hash

    def pattern_matching(self, text, pattern):
        if pattern == '' or text == '':
            return None

        n, m = len(text), len(pattern),
        if m > n:
            return None

        pattern_hash = self.create_hash(pattern, m - 1)
        text_hash = self.create_hash(text, m - 1)

        for i in range(1, n - m + 2):
            if pattern_hash == text_hash:
                window_text = text[i-1:i+m-1]

                if self.check_equal(window_text, pattern):
                    return i - 1

            # if i < n - m + 1:
                # text_hash = recalculate_hash(text, i-1, i+m-1, text_hash, m)
            text_hash = self.recalculate_hash(text, i, i+m, text_hash, m)

        return -1
