def fractional_knapsack(weights, profits, capacity):
    n = len(profits)
    indexes = list(range(n))

    ratios = [p/w for p, w in zip(profits, weights)]
    indexes.sort(key=lambda i: ratios[i], reverse=True)

    max_value = 0
    fractions = [0] * n

    for i in indexes:
        if weights[i] <= capacity:
            fractions[i] = 1
            max_value += profits[i]
            capacity -= weights[i]
        else:
            fractions[i] = capacity/weights[i]
            max_value += profits[i] * capacity/weights[i]
            break

    return max_value, fractions


profits = [5, 10, 15, 7, 8, 9, 4]
# profits = [60, 100, 120]
weights = [1, 3, 5, 4, 1, 3, 2]
# weights = [10, 20, 30]
capacity = 15
# capacity = 50
max_value, fractions = fractional_knapsack(weights, profits, capacity)
print(max_value, fractions)
