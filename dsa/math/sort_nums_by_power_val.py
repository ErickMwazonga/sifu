'''
1387. Sort Integers by The Power Value
Link: https://leetcode.com/problems/sort-integers-by-the-power-value/

The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:
if x is even then x = x / 2
if x is odd then x = 3 * x + 1

For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, 
if two or more integers have the same power value sort them by ascending order.

Return the kth integer in the range [lo, hi] sorted by the power value.
Notice that for any integer x (lo <= x <= hi) it is guaranteed that 
x will transform into 1 using these steps and that the power of x is will fit in a 32-bit signed integer.

Example:
Input: lo = 12, hi = 15, k = 2
Output: 13

Explanation: The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1)
The power of 13 is 9
The power of 14 is 17
The power of 15 is 17
The interval sorted by the power value [12, 13, 14, 15]. 
For k = 2 answer is the second element which is 13.
Notice that 12 and 13 have the same power value and we sorted them in ascending order. Same for 14 and 15.
'''

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers: list[tuple(int, int)] = []
            
        for num in range(lo, hi + 1):
            power = self.getPower(num)
            # power = self.getPower_v2(num, 0)
            # power = self.getPower_v2(num, 0, cache={})

            powers.append((power, num))
            
        powers.sort()
        
        target = powers[k-1]
        return target[1]
    
    def getPower(self, N: int) -> int:  
        count = 0
        
        while N != 1:
            is_even = N % 2 == 0
            N = N // 2 if is_even else (3 * N) + 1

            count += 1
            
        return count

    def getPower_v2(self, num: int, count: int) -> int:
        if num == 1:
            return count
        
        if num % 2 == 0:
            return self.getPower_v2(num // 2, count + 1)
        else:
            return self.getPower_v2(3 *num + 1, count + 1)

    def getPower_v3(self, num: int, count: int, cache: dict[int, int]) -> int:
        if num == 1:
            return count
        
        if num in cache:
            return count
        
        is_even = num % 2 == 0
        num = num // 2 if is_even else (3 * num) + 1
        
        power = self.getPower_v2(num, count + 1, cache)
            
        cache[num] = power
        return power
        
                