'''
374. Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower/

We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:
-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.
'''


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = (l + r) // 2
            status = self.guessNumber(m)

            if status == 0:
                return m
            elif status == 1:
                l = m + 1
            else:
                r = m - 1
