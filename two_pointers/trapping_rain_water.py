'''
42. Trapping Rain Water
Link: https://leetcode.com/problems/trapping-rain-water/
Resource: https://www.youtube.com/watch?v=RV7jsfvJ33U&list=PLDMSG_DkY6zf4splOszM3iyPUeDQ_-3o5&index=26

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
1. [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] ->  6
Explanation: The above elevation map (black section) is represented by array
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]. In this case,  6 units of rain water (blue section) are being trapped.

Example 2:
1. [4, 2, 0, 3, 2, 5] -> 9
'''


def trap(heights: list[int]) -> int:
    left, right = 0, len(heights) - 1
    max_water = 0

    maxLeft = maxRight = 0

    while left <= right:
        if heights[left] <= heights[right]:
            maxLeft = max(maxLeft, heights[left])
            max_water += maxLeft - heights[left]
            left += 1
        else:
            maxRight = max(maxRight, heights[right])
            max_water += maxRight - heights[right]
            right += 1

    return max_water


def trap_v2(heights):
    left, right = 0, len(heights) - 1
    water = 0

    maxLeft = heights[left]
    maxRight = heights[right]

    while left < right:
        if heights[left] <= heights[right]:
            left = left + 1
            maxLeft = max(maxLeft, heights[left])
            water += maxLeft - heights[left]
        else:
            right = right - 1
            maxRight = max(maxRight, heights[right])
            water += maxRight - heights[right]

    return water


assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert trap([4, 2, 0, 3, 2, 5]) == 9
