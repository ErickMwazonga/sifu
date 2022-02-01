'''
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
'''


def maxArea(heights: list[int]) -> int:
    i, j = 0, len(heights) - 1
    max_area = 0

    while i <= j:
        area_width = j - i
        base_height = min(heights[i], heights[j])

        current_area = area_width * base_height
        max_area = max(max_area, current_area)

        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1

    return max_area
