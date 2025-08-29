'''
84. Largest Rectangle in Histogram
Link - https://leetcode.com/problems/largest-rectangle-in-histogram
INTUITION - https://www.youtube.com/watch?v=zx5Sw9130L0&list=PLot-Xpze53lfxD6l5pAGvCD4nPvWKU8Qo

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2, 1, 5, 6, 2, 3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2, 4]
Output: 4
'''

def largestRectangleArea(heights: list[int]) -> int:
    max_area = 0
    stack = []

    for i, height in enumerate(heights):
        if not stack:
            stack.append([i, height])
            continue

        start = i
        while stack and stack[-1][1] > height:
            start, top_height = stack.pop()
            max_area = max(max_area, (i - start) * top_height)

        stack.append([start, height])

    while stack:
        idx, top_height = stack.pop()
        spread_area = (len(heights) - idx) * top_height 
        # spread_area = (i - idx + 1) * top_height
        max_area = max(max_area, spread_area) 


def largestRectangleArea_v2(heights: list[int]) -> int:
    maxArea = 0
    stack = []

    for index, height in enumerate(heights):
        start = index

        # Check if the stack is not empty and the height at the top of the stack is greater than the current height
        while start and stack[-1][1] > height:
            i, h = stack.pop()
            # Calculate the area for the popped element and update maxArea if needed
            maxArea = max(maxArea, (index - i) * h)
            start = i

        # Push the current index and height onto the stack
        stack.append((start, height))

    # Process any remaining elements in the stack
    for index, height in stack:
        maxArea = max(maxArea, (len(heights) - index) * height)

    return maxArea