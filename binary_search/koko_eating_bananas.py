'''
875. Koko Eating Bananas
Link: https://leetcode.com/problems/koko-eating-bananas/

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3, 6, 7, 11],  h = 8
Output: 4

Example 2:
Input: piles = [30, 11, 23, 4, 20], h = 5
Output: 30
'''

import math

class Solution:
    '''Time: O(n * log(max(piles)))'''

    def minEatingSpeed(self, piles: list[int], H: int) -> int:
        l, r = 1, max(piles)
        k = 0

        while l <= r:
            m = (l + r) // 2

            if self.k_works(piles, m, H):
                k = m
                r = m - 1
            else:
                l = m + 1

        return k
    
    def k_works(self, piles, k, H):
        totalTime = 0
        for p in piles:
            totalTime += math.ceil(p / k)

        return totalTime <= H
