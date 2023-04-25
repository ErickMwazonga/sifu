'''
H-Tree Construction
https://www.pramp.com/challenge/EmYgnOgVd4IElnjAnQqn

An H-tree is a geometric shape that consists of a repeating pattern resembles the letter “H”.
It can be constructed by starting with a line segment of arbitrary length, 
drawing two segments of the same length at right angles to the first through its endpoints, 
and continuing in the same vein, reducing (dividing) the length of the line segments drawn at each stage by √2.

Here are some examples of H-trees at different levels of depth:

Write a function drawHTree that constructs an H-tree, given its center (x and y coordinates), a starting length, and depth. 
Assume that the starting line is parallel to the X-axis.

Use the function drawLine provided to implement your algorithm. In a production code, a drawLine function would render a real line between two points. 
However, this is not a real production environment, so to make things easier, 
implement drawLine such that it simply prints its arguments (the print format is left to your discretion).

Analyze the time and space complexity of your algorithm. In your analysis, 
assume that drawLine's time and space complexities are constant, i.e. O(1).
'''

import math

def drawTree(x: int, y: int, length: int, depth: int) -> None:
	if depth == 0:
		return

	x0, y0 = x - length/2, y - length/2
	x1, y1 = x + length/2, y + length/2

	drawLine(x0, y0, x0, y1)
	drawLine(x1, y0, x1, y1)
	drawLine(x0, y, x1, y)

	new_length = length / math.sqrt(2)

	drawHTree(x0, y0, new_length, depth-1)
	drawHTree(x0, y1, new_length, depth-1)
	drawHTree(x1, y0, new_length, depth-1)
	drawHTree(x1, y1, new_length, depth-1)


def drawLine(x1, y1, x2, y2):
  	print([x1, y1], [x2, y2])
