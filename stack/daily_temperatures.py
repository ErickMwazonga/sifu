'''
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Given a list of daily temperatures T, return a list such that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
'''

def dailyTemperatures(temps):
    n = len(temps)
    days_to_wait = [0] * n
    stack = []  # indexes from hottest to coldest

    for i in range(n-1, -1, -1):
        while stack and temps[i] >= temps[stack[-1]]:
            stack.pop() # remove lower and not soonest 

        if stack:
            days_to_wait[i] = stack[-1] - i
        stack.append(i)

    return days_to_wait
    
def dailyTemperatures(temperatures):
    n = len(temperatures)
    days_to_wait, stack = [0] * n, []

    for i in range(n-1, -1, -1):
        if stack == []:
            stack.append(i)
        else:
            while stack and temperatures[stack[-1]] < temperatures[i]:
                stack.pop()
            days_to_wait[i] = stack[-1] - i if stack != [] else 0
            stack.append(i)
    
    return days_to_wait
