'''
1408. String Matching in an Array
https://leetcode.com/problems/string-matching-in-an-array/

Given an array of string words. Return all strings in words which is substring of another word in any order.
String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

Example 1:
1. ['mass', 'as', 'hero', 'superhero'] -> ['as', 'hero']
    Explanation: 'as' is substring of 'mass' and 'hero' is substring of 'superhero'.
    ['hero', 'as'] is also a valid answer.

2. ['leetcode', 'et', 'code'] -> ['et', 'code']
    Explanation: 'et', 'code' are substring of 'leetcode'.

3. ['blue', 'green', 'bu'] -> []
'''


class Solution:

    def stringMatching(self, words):
        a = ' '.join(words)
        return [w for w in words if a.count(w) > 1]

    def stringMatching_v2(self, words):
        res = []

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])

        return set(res)


class Solution_V2:
    '''
    Time: O(N * M), Space: O(M)
    N - count of words, M - size of the word
    '''

    def stringMatching(self, words):
        n, res = len(words), []

        for i in range(n):
            for j in range(n):
                if i != j:
                    text, pattern = words[j], words[i]

                    if self.is_a_match(text, pattern):
                        res.append(pattern)
                        break

        return res

    def is_a_match(self, text, pattern):
        i, j = 0, 0
        lps = self.build_lps(pattern)

        while i < len(text):
            if text[i] == pattern[j]:
                i, j = i + 1, j + 1

                if j == len(pattern):
                    return True
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]

        return False

    def build_lps(self, pattern):
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
