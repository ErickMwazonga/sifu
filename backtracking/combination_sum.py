'''
39. Combination Sum
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times. 7 is a candidate, and 7 = 7.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2], [2,3,3], [3,5]]
'''


class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []

        self.helper(candidates, target, res, cur_subset=[], index=0)

        return res

    def helper(self, candidates, remain, res, cur_subset, index):
        if remain == 0:
            return res.append(cur_subset)

        for i in range(index, len(candidates)):
            if candidates[i] > remain:
                return

            cur_subset.append(candidates[i])
            self.helper(candidates, remain - candidates[i], res, cur_subset, i)
            cur_subset.pop()


class Solution_V2:
    def combinationSum(self, candidates, target):
        res = []
        self.helper(candidates, target, res, total=0, index=0, subset=[])

        return res

    def helper(self, cands, target, res, total, index, subset):
        if total == target:
            res.append(subset[:])
            return

        if index >= len(cands) or total > target:
            return

        subset.append(cands[index])
        self.helper(cands, target, res, total + cands[index], index, subset)
        subset.pop()

        self.helper(cands, target, res, total, index + 1, subset)
