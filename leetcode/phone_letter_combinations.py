class Solution:
    '''
    # Time:  O(n * 4^n)
    # Space: O(n)
    '''
    def letterCombinations(self, digits: str) -> List[str]:
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
        
        if len(digits) == 0:
            return []
        
        if len(digits) == 1:
            return list(mapping[digits[0]])
        
        all_combinations = list(mapping[digits[0]])
        
        for i in range(1, len(digits)):
            current_combinations = []
            
            for combination in all_combinations:
                for letter in mapping[digits[i]]:
                    current_combinations.append(f'{combination}{letter}')
                    
            all_combinations = current_combinations
        
        return all_combinations
        

class Solution(object):
    '''
    # Time:  O(n * 4^n)
    # Space: O(n)
    '''

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