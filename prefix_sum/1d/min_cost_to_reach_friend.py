'''
Minimum Cost To Reach Your Friend
https://leetcode.com/discuss/post/7014919/minimum-cost-to-reach-your-friend-by-sau-229r/

You are given an array of integers nums, where each number may appear multiple times.
Every time a number appears more than once, it represents friends trying to meet — that is,
each number corresponds to a group of friends with the same name (number).

When two friends with the same number try to meet, the cost is defined as the sum of all elements strictly between their positions in the array.
If this sum is negative, the cost is treated as 0 (as if the path was magically shortened).
🔹 For each group of friends (same number), find the minimum possible cost for any two of them to meet.
🔹 Return the total cost required for all such groups.

✅ Example 1
Input: nums = [1, 5, -2, 1, 5]
Output: 3

Explanation:
Friends with number 1 at indices 0 and 3 → sum between = 5 + (-2) = 3 → cost = 3
Friends with number 5 at indices 1 and 4 → sum between = -2 + 1 = -1 → cost = 0
Total cost = 3 + 0 = 3

✅ Example 2
Input: nums = [3, 2, -4, 3, 2]
Output: 0

Explanation:
Two friends with number 3 at indices 0 and 3 → sum between = 2 + (-4) = -2 → cost = 0
Two friends with number 2 at indices 1 and 4 → sum between = -4 + 3 = -1 → cost = 0
Total cost = 0 + 0 = 0

✅ Example 3
Input: nums = [7, -1, 4, 7, 4, -2, 7]
Output: 2

Explanation:
Friends with number 7 at indices 0, 3, 6:
Cost between 0 and 3 = 3
Cost between 3 and 6 = 2 → minimum = 2
Friends with number 4 at indices 2 and 4 → sum = 7 → cost = 7
Total cost = 2 + 7 = 9

# INTUITION
1. Use prefix sums to calculate the sum of elements between two indices efficiently.
2. Group indices by their corresponding number.
3. For each group, calculate the minimum cost for any two friends to meet.
'''

from collections import defaultdict

def min_total_cost(nums):
    n = len(nums)

    # Step 1: Compute prefix sum
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # Step 2: Group indices by number
    indices_by_number = defaultdict(list)
    for i, num in enumerate(nums):
        indices_by_number[num].append(i)

    total_cost = 0

    # Step 3: For each group of same numbers, compute minimum pairwise cost
    for num, indices in indices_by_number.items():
        if len(indices) < 2:
            continue  # Only one friend, skip

        min_cost = float('inf')
        for i in range(len(indices) - 1):
            for j in range(i + 1, len(indices)):
                left, right = indices[i], indices[j]
                cost = prefix[right] - prefix[left + 1]
                min_cost = min(min_cost, max(0, cost))

        total_cost += min_cost

    return total_cost