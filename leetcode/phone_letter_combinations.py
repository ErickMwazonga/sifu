class Solution(object):
    def letterCombinations(self, digits):
        sol = []
        if len(digits) == 0:
            return sol
        self.letterCombinationsHelper(digits, '', sol)
        return sol

    def letterCombinationsHelper(self, digits, currStr, sol):
        if len(digits) == 0:
            sol.append(currStr)
            return

        possibleChars = self.digitToLetters(digits[0])
        for ch in possibleChars:
            currStr += ch
            self.letterCombinationsHelper(digits[1:], currStr, sol)
            currStr = currStr[:-1]

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