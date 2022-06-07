'''
Given a staircase of n steps, and a set of possible steps that
can be used to climb at a time named possibleSteps,
create a function that returns the number of ways that a
person can take to reach the op of the staircase

e.g
input:
	n = 10
	possibleSteps = [2, 4, 5, 8]
output: 11
'''


def waysToClimb(n, possibleSteps):  # RECURSION
    if n == 0:
        return 1
   
    nbWays = 0

    for steps in possibleSteps:
        if (n-steps) >= 0:
            nbWays += waysToClimb(n-steps, possibleSteps)

    return nbWays


def waysToClimb_v2(n, possibleSteps, lookup):  # MEMOIZATION - TOP-DOWN APPROACH
    key = str(n)

    if key in lookup:
        return lookup[key]

    if n == 0:
        lookup[key] = 1
        return lookup[key]
    
    nbWays = 0
    for steps in possibleSteps:
        if (n-steps) >= 0:
            nbWays += waysToClimb_v2(n-steps, possibleSteps)
    
    lookup[key] = nbWays
    return lookup[key]


def waysToClimb(n, possibleSteps):  # DYNAMIC PROGRAMMING - BOTTOM-UP APPROACH
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, len(dp)):
        nbWays = 0

        for steps in possibleSteps:
            if (i-steps) >= 0:
                nbWays += dp[i-steps]
        dp[i] = nbWays

    return dp[n]
