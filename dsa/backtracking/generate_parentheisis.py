'''
22. Generate Parentheses
Link: https://leetcode.com/problems/generate-parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Examples
1. 3 -> ['((()))', '(()())', '(())()', '()(())', '()()()']
2. 1 ->  ['()']
'''


class Solution:
    '''
    Time: O(n * 2^n), Space: O(n * 2^n)
    Time: The tree has a max height of 2n, therefore the max nodes the tree has is 2 ^ 2n.
    Therefore the time complexity is O(2^2n) = O(4^n).
    Space: We have 2^(2n-1) leaves at most, therefore, the time complexity is O(4^n).
    '''

    def generateParenthesis(self, n: int):
        # only add open paranthesis if open < n
        # only ad closing parenthesis if closed < open
        # valid IFF open == closed == n

        res, comb = [], ''
        self.dfs(n, res, comb, _open=0, close=0)
        return res

    def dfs(self, n, res, comb, _open, close):
        if _open == close == n:
            res.append(comb)
            return

        if _open < n:
            self.dfs(n, res, comb + '(', _open + 1, close)

        if close < _open:
            self.dfs(n, res, comb + ')', _open, close + 1)


class Solution_V2:

    def generateParenthesis(self, n):
        res = []
        self.dfs(res, _open=n, close=n, combo='')
        return res

    def dfs(self, res, _open, close, combo):
        if close < _open:
            return

        if not _open and not close:
            res.append(combo)
            return

        if _open:
            self.dfs(res, _open-1, close, combo + '(')
            
        if close:
            self.dfs(res, _open, close-1, combo + ')')
