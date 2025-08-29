'''
1309. Decrypt String from Alphabet to Integer Mapping
Link: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.

Examples:
1. '10#11#12' -> 'jkab'
    Explanation: 'j' -> '10#' , 'k' -> '11#' , 'a' -> '1' , 'b' -> '2'.

2 '1326#' -> 'acz'
'''

from string import ascii_lowercase


class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''
        i, n = 0, len(s)
        
        while i < n:
            j = i
            
            while j < n and s[j] != '#':
                j += 1
                
            string = s[i:j+1]
            res += self.get_characters(string)
        
            i = j + 1
            
        return res
        
    def get_characters(self, s: str) -> str:
        # s_list = list(map(lambda x: f'{x}#', s_list))
        
        val = lambda i: str(i) if i < 10 else f'{i}#'
        mapping = {val(i): ch for i, ch in enumerate(ascii_lowercase, 1)}
                
        if not s:
            return ''
        
        if s in mapping:
            return mapping[s]
        
        res = ''
        last_mapping = ''

        if s[-1] == '#':
            last_two_chars = s[-3:]
            last_mapping = mapping[last_two_chars]
            s = s[:-3]

        for ch in s:
            res += mapping[ch]

        res += last_mapping
       
        return res
    