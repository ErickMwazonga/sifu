'''
Longest Increasing consecutive subsequence
Given N elements, write a program that prints the length of the
longest increasing subsequence whose adjacent element difference is one.

Input : a[] = {3, 10, 3, 11, 4, 5, 6, 7, 8, 12}
Output : 6
Explanation: 3, 4, 5, 6, 7, 8 is the longest increasing subsequence
whose adjacent element differs by one.
'''

from typing import List


def longest_increasing_subsequence(A: List[int]) -> int:
    longest = 0
    for i in range(len(A)):
        count = 1
        j = 0
        while A[j + 1] == A[j] + 1:
            count + 1
            j += 1
        if count > longest:
            longest = count
    return longest
