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

# RECURSION
def waysToClimb(n, possibleSteps):
	if n == 0:
		return 1
	else:
		nbWays = 0

		for steps in possibleSteps:
			if (n-steps) >= 0:
				nbWays += waysToClimb(n-steps, possibleSteps)

	return nbWays

# MEMOIZATION - TOP-DOWN APPROACH
def waysToClimb(n, possibleSteps, lookup):
	key = str(n)

	if key in lookup:
		return lookup[key]
	elif n == 0:
		lookup[key] = 1
		return lookup[key]
	else:
		nbWays = 0
		for steps in possibleSteps:
			if (n-steps) >= 0:
				nbWays += waysToClimb(n-steps, possibleSteps)
		lookup[key] = nbWays

		return lookup[key]

# DYNAMIC PROGRAMMING - BOTTOM-UP APPROACH
def waysToClimb(n, possibleSteps):
	dp = [0] * (n + 1)
	dp[0] = 1
	
	for i in range(1, len(dp)):
		nbWays = 0

		for steps in possibleSteps:
			if (i-steps) >= 0:
			nbWays += dp[i-steps]
		dp[i] = nbWays

	return dp[n]