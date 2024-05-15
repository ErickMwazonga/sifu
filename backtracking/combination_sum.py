'''
39. Combination Sum
Link: https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Example 1:
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]

Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times. 7 is a candidate, and 7 = 7.

Example 2:
Input: candidates = [2, 3, 5],  target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
'''


class Solution:
    def combinationSum(self, candidates, target):
        res = []
        self.dfs(candidates, target, res, total=0, idx=0, subset=[])
        return res

    def dfs(self, cands, target, res, total, idx, subset):
        if total == target:
            res.append(subset[:])
            return

        if idx >= len(cands) or total > target:
            return

        for i in range(idx, len(cands)):
            subset.append(cands[i])
            self.dfs(cands, target, res, total + cands[i], i, subset)
            subset.pop()


class Solution_V2:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []

        self.helper(candidates, target, res, subset=[], idx=0)

        return res

    def helper(self, candidates, remain, res, subset, idx):
        if remain == 0:
            return res.append(subset)

        for i in range(idx, len(candidates)):
            if candidates[i] > remain:
                return

            subset.append(candidates[i])
            self.helper(candidates, remain - candidates[i], res, subset, i)
            subset.pop()
