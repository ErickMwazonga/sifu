'''
22. Generate Parentheses
Link: https://leetcode.com/problems/generate-parentheses/submissions/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Examples
1. 3 -> ['((()))', '(()())', '(())()', '()(())', '()()()']
2. 1 ->  ['()']
'''


class Solution:
    '''
    Time: O(n * 2^n), Space: O(n * 2^n)
    Time: The tree has a max height of 2n, therefore the max nodes the tree has is 2 ^ 2n. Therefore the time complexity is O(2^ 2n)=O(4^n).
    Space: We have 2^(2n-1) leaves at most, therefore, the time complexity is O(4^n).
    '''

    def generateParenthesis(self, n: int):
        # only add open paranthesis if open < n
        # only ad closing parenthesis if closed < open
        # valid IFF open == closed == n

        res, stack = [], ''
        self.backtrack(n, res, stack, openN=0, closedN=0)
        return res

    def backtrack(self, n, res, stack, openN, closedN):
        if openN == closedN == n:
            res.append(stack)
            return

        if openN < n:
            self.backtrack(n, res, stack + '(', openN + 1, closedN)

        if closedN < openN:
            self.backtrack(n, res, stack + ')', openN, closedN + 1)


class Solution_V2:

    def generateParenthesis(self, n):
        if not n:
            return []

        left, right = n, n
        res = []
        self.dfs(left, right, res, '')
        return res

    def dfs(self, left, right, res, combo):
        if right < left:
            return
        if not left and not right:
            res.append(combo)
            return

        if left:
            self.dfs(left-1, right, res, combo + '(')
        if right:
            self.dfs(left, right-1, res, combo + ')')
