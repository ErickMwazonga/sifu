'''
264. Ugly Number II
https://leetcode.com/problems/ugly-number-ii/

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.

Examples:
1. 10 -> 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

1. 1 -> 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
'''

import heapq


def nthUglyNumber(n: int) -> int:
    ugly = [1]
    i2, i3, i5 = 0, 0, 0

    while n > 1:
        u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]

        umin = min((u2, u3, u5))
        ugly.append(umin)

        if umin == u2:
            i2 += 1
        if umin == u3:
            i3 += 1
        if umin == u5:
            i5 += 1

        n -= 1

    return ugly[-1]


def nthUglyNumber(n: int) -> int:
    '''Time: O(Nlog(N)), Space: O(N)'''

    heap = [1]
    visited = set([1])

    current_ugly = 1

    for _ in range(n):
        current_ugly = heapq.heappop(heap)

        for factor in [2, 3, 5]:
            new_ugly = current_ugly * factor

            if new_ugly not in visited:
                visited.add(new_ugly)
                heapq.heappush(heap, new_ugly)

    return current_ugly
