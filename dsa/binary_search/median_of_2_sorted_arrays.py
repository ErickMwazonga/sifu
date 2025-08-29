'''
4. Median of Two Sorted Arrays
Link - https://leetcode.com/problems/median-of-two-sorted-arrays/
Resource - [https://www.youtube.com/watch?v=LPFhl65R7ww, https://www.youtube.com/watch?v=q6IEA26hvXc]

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''


def get_median(nums: list[int]) -> float:
    N = len(nums)

    if N % 2:
        return nums[N // 2]

    K = N // 2
    return (nums[K - 1] + nums[K]) / 2


class Solution_V1:

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_arr = sorted(nums1 + nums2)
        return get_median(merged_arr)


class Solution_V2:

    def findMedianSortedArrays(self, A: list[int], B: list[int]) -> float:
        n, m = len(A), len(B)
        i, j, k = 0, 0, 0
        merged_arr = [0] * (n + m)

        while i < n and j < m:
            if A[i] < B[j]:
                merged_arr[k] = A[i]
                i, k = i + 1, k + 1
            else:
                merged_arr[k] = B[j]
                j, k = j + 1, k + 1

        while i < n:
            merged_arr[k] = A[i]
            i, k = i + 1, k + 1

        while j < m:
            merged_arr[k] = B[j]
            j, k = j + 1, k + 1

        return get_median(merged_arr)


class Solution_v3:

    def findMedianSortedArrays(self, input1: list[int], input2: list[int]):
        N, M = len(input1), len(input2)
        total = N + M

        if N > M:
            return self.findMedianSortedArrays(input2, input1)

        low, high = 0, N
        while low <= high:
            partX = (low + high) // 2  # partitionX and partitionY
            # no. elements need to be the same in both partitions of both arrs
            partY = (total + 1) // 2 - partX

            # if partitionX is 0 -> there's nothing on left side -> maxLeftX = -inf
            # if partitionX is N -> there's nothing on right side-> minRightX = +inf

            maxLeftX = float('-inf') if partX == 0 else input1[partX - 1]
            minRightX = float('inf') if partX == N else input1[partX]

            maxLeftY = float('-inf') if partY == 0 else input2[partY - 1]
            minRightY = float('inf') if partY == M else input2[partY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if total % 2:
                    return max(maxLeftX, maxLeftY)
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2

            if maxLeftX > minRightY:
                high = partX - 1
            else:
                low = partX + 1
