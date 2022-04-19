'''
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Examples:
1. '23' -> ['ad','ae','af','bd','be','bf','cd','ce','cf']
2. '' -> []
3. '2' -> ['a','b','c']
'''


class Solution:
    '''
    Time:  O(n * 4^n), # Space: O(n)
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/1022553/Python-3-approaches-(iterative-DFS-BFS-recursive)-%3A-visuals-%2B-explanation
    '''

    def letterCombinations(self, digits):
        if not digits:
            return []

        res = []
        self.dfs(digits, res, curr_str='', i=0)
        return res

    def dfs(self, digits, res, curr_str, i):
        if len(curr_str) == len(digits):
            res.append(curr_str)
            return

        nextDigit = digits[i]
        possibleChars = self.digitToLetters(nextDigit)
        for ch in possibleChars:
            self.dfs(digits, res, curr_str + ch, i + 1)

    def digitToLetters(self, digit):
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        return mapping[digit]


class Solution:
    '''# Time:  O(n * 4^n), # Space: O(n) '''

    def letterCombinations(self, digits: str) -> list[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        n = len(digits)
        if n == 0:
            return []

        if n == 1:
            return list(mapping[digits[0]])

        all_combinations = list(mapping[digits[0]])

        for i in range(1, n):
            current_combinations = []
            current_letters = mapping[digits[i]]

            for combination in all_combinations:
                for letter in current_letters:
                    current_combinations.append(f'{combination}{letter}')

            all_combinations = current_combinations

        return all_combinations


def letterCombinations(digits: str):
    if not digits:
        return []

    d = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def recursive(i=0, combo='', res=[]):
        if i == len(digits):
            res.append(combo)
        else:
            nextDigit = digits[i]
            children = d[nextDigit]

            for child in children:
                recursive(i+1, combo+child, res)

        return res

    return recursive(0, "", [])
