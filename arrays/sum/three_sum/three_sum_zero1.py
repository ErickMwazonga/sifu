"""
Question - Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

def three_sum_zero(arr):
    res = []
    arr.sort()
    length = len(arr)

    for i in range(length-2):
        if i == 0 or (arr[i] > arr[i-1]):
            start = i + 1
            end = length - 1

            while(start < end):
                tot = arr[i] + arr[start] + arr[end]
                if tot == 0:
                    res.append([arr[i], arr[start], arr[end]])

                if tot < 0:
                    curr_start = start
                    while (arr[start] == arr[curr_start]) and (start < end):
                        start += 1
                else:
                    curr_end = end
                    while (arr[end] == arr[curr_end]) and (end < end):
                        end -= 1

    return res
    

a = [-1, 0, 1, 2, -1, -4]

print(three_sum_zero(a))