'''
223. Rectangle Area
https://leetcode.com/problems/rectangle-area/

Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).
The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).
'''


def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) -> int:
    '''https://leetcode.com/problems/rectangle-area/discuss/1664235/Python-Solution-for-Coding-Kids'''

    first_area = (ax2 - ax1) * (ay2 - ay1)
    second_area = (bx2 - bx1) * (by2 - by1)

    # overlap
    left = max(ax1, bx1)
    right = min(ax2, bx2)
    bottom = max(ay1, by1)
    top = min(ay2, by2)

    width = max(right - left, 0)
    height = max(top - bottom, 0)
    overlap = width * height

    return first_area + second_area - overlap
