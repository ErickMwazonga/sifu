'''
28. Implement strStr()

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Examples:
Input: haystack = "hello", needle = "ll"
Output: 2

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Input: haystack = "", needle = ""
Output: 0

ALGORITHM
The Rabin–Karp algorithm or Karp–Rabin algorithm is a string-searching algorithm
created by Richard M. Karp and Michael O. Rabin (1987)
that uses hashing to find an exact match of a pattern string in a text.
It uses a rolling hash to quickly filter out positions of the text that cannot match the pattern,
and then checks for a match at the remaining positions. Generalizations of the same idea can be
used to find more than one match of a single pattern, or to find matches for more than one pattern.
'''


class Solution:
    def __init__(self):
        self.base = 26  # base of the polynomial hash
        self.prime_mod = 101  # to avoid hash overflow, doesn't have to be prime number

    def charcode(self, ch):
        return ord(ch) - ord('a')

    def myhash(self, s):
        '''polynomial hash of a string'''

        my_hash = 0
        for ch in s:
            my_hash = (charcode(ch) + my_hash * self.base) % self.prime_mod
        return my_hash

    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        N = len(needle)

        needle_hash = self.myhash(needle)
        rolling_hash = self.myhash(haystack[:N-1])

        # the first digit's base as a const, to avoid recomputation
        first_pow = self.base ** (N-1)

        for i in range(N-1, len(haystack)):
            code = charcode(haystack[i])
            rolling_hash = (rolling_hash * self.base + code) % self.prime_mod

            if rolling_hash == needle_hash and needle == haystack[i+1-N:i+1]:
                return i+1-N

            prev_code = charcode(haystack[i+1-N])
            rolling_hash = (rolling_hash - prev_code *
                            first_pow) % self.prime_mod

        return -1
