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
    left, right = max(ax1, bx1), min(ax2, bx2)
    bottom, top = max(ay1, by1),  min(ay2, by2)

    # What if the areas are apart
    width, height = max(right - left, 0), max(top - bottom, 0)
    overlap_area = width * height

    return first_area + second_area - overlap_area


def computeArea_v2(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    left, right = max(ax1, bx1), min(ax2, bx2)
    bottom, top = max(ay1, by1), min(ay2, by2)

    width = right - left
    if width < 0:
        width = 0

    height = top - bottom
    if height < 0:
        height = 0

    overlap_area = width * height

    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)

    return (area_a + area_b) - overlap_area
