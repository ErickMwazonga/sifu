'''
593. Valid Square
Link: https://leetcode.com/problems/valid-square/description/

Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.
The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.
A valid square has four equal sides with positive length and four equal angles (90-degree angles).

Examples:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false

Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true

[INTUITION]
For a valid square:
- All lengths should be equal hence just 1 entry to the set
- Both diagonals should be equal hence the second entry to the set
- None of the lengths/diagonals should be 0
'''

from collections import namedtuple


def d(point1, point2):
    '''length = (x1-x2)^2 + (y1-y2)^2'''

    Point = namedtuple('Point', 'x,y')
    p1, p2 = Point(*p1), Point(*p2)

    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def validSquare(p1, p2, p3, p4) -> bool:
    lengths = [
        d(p1, p2), d(p1, p3), d(p1, p4), d(p2, p3), d(p2, p4), d(p3, p4)
    ]

    lengths = set(lengths)

    no_points_are_at_the_same_location = 0 not in lengths
    only_diagonals_and_sides = len(lengths) == 2

    return no_points_are_at_the_same_location and only_diagonals_and_sides


assert validSquare([0, 0], [1, 1], [1, 0], [0, 1]) == True
assert validSquare([0, 0], [1, 1], [1, 0], [0, 12]) == False
assert validSquare([1, 0], [-1, 0], [0, 1], [0, -1]) == True
