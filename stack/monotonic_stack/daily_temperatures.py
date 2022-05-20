'''
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/
Resource: https://www.youtube.com/watch?v=cTBiBSnjO3c

Given a list of daily temperatures T, return a list such that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
'''


def dailyTemperatures(temperatures):
    n = len(temperatures)
    res = [0] * n
    stack = []  # (tem, index)

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stack_temp, stack_idx = stack.pop()
            res[stack_idx] = i - stack_idx

        stack.append((t, i))

    return res
