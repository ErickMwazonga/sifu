'''
473. Matchsticks to Square
Link: https://leetcode.com/problems/matchsticks-to-square/
Resource: https://www.youtube.com/watch?v=hUe0cUKV-YY

You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick.
You want to use all the matchsticks to make one square. You should not break any stick,
but you can link them up, and each matchstick must be used exactly one time.
Return true if you can make this square and false otherwise.

Examples:
1. [1, 1, 2, 2, 2] -> True
    Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

2. [3, 3, 3, 3, 4] -> False
    Explanation: You cannot find a way to form a square with all the matchsticks.
'''


class Solution:

    def makesquare(self, matchsticks) -> bool:
        target = sum(matchsticks) // 4
        sides = [0] * 4

        if sum(matchsticks) / 4 != target:
            return False

        matchsticks.sort(reverse=True)

        return self.backtrack(matchsticks, sides, i=0, target=target)

    def backtrack(self, matchsticks, sides, i, target):
        if i == len(matchsticks):
            return True

        for j in range(4):
            if sides[j] + matchsticks[i] > target:
                continue

            sides[j] += matchsticks[i]
            if self.backtrack(matchsticks, sides, i + 1, target):
                return True

            sides[j] -= matchsticks[i]

        return False
