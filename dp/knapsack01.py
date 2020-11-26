# Input:
# Values (stored in list v)
# Weights (stored in list w)
# Number of distinct items (n)
# Knapsack capacity (W)

def knapSack(values, w, W):
    n = len(values)

    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for j in range(W + 1):
            current_weight = w[i - 1]
            current_val = values[i - 1]
            rem_weight = j - current_weight

            # don't include ith element if j-w[i-1] is negative
            if current_weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
				# find maximum value we get by excluding or including the ith item
                # max of exclude vs include
				dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i - 1][rem_weight] + current_val
                )

	# return maximum value
	return dp[n][W]


if __name__ == '__main__':

	# Input: set of items each with a weight and a value
	v = [20, 5, 10, 40, 15, 25]
	w = [1, 2, 3, 8, 7, 4]

	# Knapsack capacity
	W = 10

	print("Knapsack value is", knapSack(v, w, W))