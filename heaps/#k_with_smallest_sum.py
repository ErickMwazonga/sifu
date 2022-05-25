'''
373. Find K Pairs with Smallest Sums
Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2], [1,4], [1,6]]
Explanation: The first 3 pairs from: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1], [1,1]]
Explanation: The first 2 pairs from: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
'''


def k_smallest_pairs(nums1, nums2, k: int):  # NAIVE APPROACH
    result = []

    for i in nums1:
        for x in nums2:
            result.append([i, x])

    return sorted(result, key=sum)[:k]
