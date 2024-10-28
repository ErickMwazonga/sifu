'''
Find a triplet such that sum of two numbers equals to third element

Given an array of integers, you have to find three numbers such that the sum of two elements equals the third element.

Example:
Input -> [21, 13, 47, 61, 34, 40, 55, 71, 87]
Output -> [
    (21, 13, 34),
    (21, 40, 61),
    (21, 34, 55),
    (13, 34, 47),
    (47, 40, 87)
]
'''

def find_triplet_adding_to_sum(arr: list[int]) -> list[int]:
    '''Time: O(n^2), Space: O(n)'''

    nums_set, n = set(arr), len(arr)
    res = []

    for i in range(n - 1):
        for j in range(i + 1, n):
            curr_sum = arr[i] + arr[j]
            if curr_sum in nums_set:
                res.append((arr[i], arr[j], curr_sum))

    return res


def find_triplet_adding_to_sum_v2(arr: list[int]) -> list[int]:
    '''
    Time: O(n^2), Space: O(1)
    FLAW: Doesn't factor in duplicates
    '''

    arr.sort()
    i, res = len(arr) - 1, []

    while i >= 0:
        left, right = 0, i - 1

        while left < right:
            curr_sum = arr[left] + arr[right]
            if curr_sum == arr[i]:
                res.append((arr[left], arr[right], arr[i]))
                left, right = left + 1, right - 1
            elif curr_sum < arr[i]:
                left += 1
            else:
                right -= 1

        i -= 1

    return res


def find_triplet_adding_to_sum_v3(arr: list[int]) -> list[int]:
    '''
    Time: O(n^2), Space: O(1)
    STRENGTH: HANDLES DUPLICATES
    '''

    arr.sort()
    i, res = len(arr) - 1, []

    while i >= 0:
        left, right = 0, i - 1

        while left < right:
            curr_sum = arr[left] + arr[right]
            if curr_sum == arr[i]:
                res.append((arr[left], arr[right], arr[i]))

                # Handle duplicates
                while left + 1 < right and arr[left] == arr[left + 1]:
                    res.append((arr[left], arr[right], arr[i]))
                    left += 1

                while right - 1 > left and arr[right] == arr[right - 1]:
                    res.append((arr[left], arr[right], arr[i]))
                    right -= 1

                left, right = left + 1, right - 1
            elif curr_sum < arr[i]:
                left += 1
            else:
                right -= 1

        i -= 1

    return res


class Solution:
    '''Time: O(N^2), Space: O(N)'''

    def find_triplets(self, arr):
        triplets = []
        self._helper(arr, 0, [], triplets)
        return triplets

    def _helper(self, arr, start, combo, triplets):
        if len(combo) == 3:
            a, b, c = combo
            if a + b == c or a + c == b or b + c == a:
                triplets.append(tuple(combo))
            return

        for i in range(start, len(arr)):
            self._helper(arr, i + 1, combo + [arr[i]], triplets)
