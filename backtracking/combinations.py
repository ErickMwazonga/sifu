'''
77. Combinations
Link: https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output:
[
  [2, 4],
  [3, 4],
  [2, 3],
  [1, 2],
  [1, 3],
  [1, 4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
'''


class Solution:
    def combine(self, n: int, k: int):
        res = []
        self.dfs(n, k, res, start=1, combo=[])
        return res

    def dfs(self, n, k, res, start, combo):
        if len(combo) == k:
            res.append(combo[:])
            return

        for i in range(start, n+1):
            combo.append(i)
            self.dfs(n, k, res, i + 1, combo)
            combo.pop()
