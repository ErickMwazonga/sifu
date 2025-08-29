'''
128. Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Given an array of integers, find the length of the
longest sub-sequence such that elements in the subsequence are
consecutive integers, the consecutive numbers can be in any order.

Example 1
[1, 9, 3, 10, 4, 20, 2] -> 4
Explanation: The subsequence 1, 3, 4, 2 is the longest subsequence of consecutive elements

Example 2
[36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42] -> 5
Explanation: The subsequence 36, 35, 33, 34, 32 is the longest subsequence of consecutive elements.
'''


def longest_consecutive_subsequence(nums):
    if not nums:
        return 0

    nums.sort()
    current_streak, longest_streak = 1, 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

    return max(longest_streak, current_streak)


def longest_consecutive_subsequence_v2(A: list) -> int:
    '''Time: O(n), Space: O(n)'''

    visited = set(A)
    max_len = 0

    for num in A:
        count = 1
        forward = num + 1

        while forward in visited:
            count += 1
            forward += 1

        max_len = max(max_len, count)

    return max_len


def longest_consecutive_subsequence_v3(A: list) -> int:
    '''Time: O(n), Space: O(n)'''

    visited = set(A)
    max_len = 0

    for num in A:
        count = 1
        backward, forward = num - 1, num + 1

        while backward in visited:
            count += 1
            backward -= 1
        while forward in visited:
            visited.remove(forward)
            count += 1
            forward += 1
        max_len = max(max_len, count)

    return max_len

def longest_consecutive_subsequence_v4(nums):
    '''Time: O(n), Space: O(n)'''

    num_set = set(nums)
    longest_streak = 0

    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


assert longest_consecutive_subsequence([1, 9, 3, 10, 4, 20, 2]) == 4
assert longest_consecutive_subsequence([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]) == 5
assert longest_consecutive_subsequence([-1, 0, 1]) == 3
