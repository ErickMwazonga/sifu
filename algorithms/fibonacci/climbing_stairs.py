'''
70. Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Examples: 
1. 2 -> 2
    Explanation: There are two ways to climb to the top.
    1 step + 1 step
    2 steps

2. 3 -> 3
    Explanation: There are three ways to climb to the top.
    1 step + 1 step + 1 step
    1 step + 2 steps
    2 steps + 1 step

INTUITION
N = 1: [1]
N = 2: [1, 1], [2]
N = 3: [1, 2], [1, 1, 1], [2, 1]
N = 4: [1, 1, 2], [2, 2], [1, 2, 1], [1, 1, 1, 1], [2, 1, 1]

What's the relationship?
The only ways to get to N = 3, is to first get to N = 1, and then go up by 2 steps, 
or get to N = 2 and go up by 1 step. So f(3) = f(2) + f(1).
Does this hold for N = 4? Yes, it does. Since we can only get to the 4th step by getting to the 3rd step and going up by one, 
or by getting to the 2nd step and going up by two. So f(4) = f(3) + f(2).

To generalize, f(n) = f(n - 1) + f(n - 2). That's just the Fibonacci sequence!
'''


def climb_stairs(n: int) -> int:
    '''Time: O(2^n), Space: O(N)'''

    if n <= 1:
        return 1

    return climb_stairs(n - 1) + climb_stairs(n - 2)

def climb_stairs_v1(n: int) -> int:
    prev, curr = 0, 1

    for _ in range(n):
        prev, curr = curr, prev + curr

    return curr

def climb_stairs_v2(n: int) -> int:
    '''Time: O(n), Space: O(1)'''

    prev, curr = 1, 2

    for _ in range(n - 1):
        prev, curr = curr, prev + curr

    return prev

def climb_stairs_v3(n: int) -> int:
    ways = [1, 2]

    for i in range(2, n):
        distinct_ways = ways[i-1] + ways[i-2]
        ways.append(distinct_ways)

    return ways[n - 1]

def climb_stairs_fibonacci(n: int) -> int:
    dp = [0] * n

    for i in range(n):
        if i <= 2:
            dp[i] = i + 1
        else:
            dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]
