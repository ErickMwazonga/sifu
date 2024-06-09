'''
417. Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. 
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5], [3,2,3,4,4], [2,4,5,3,1], [6,7,1,4,5], [5,1,1,2,4]]
Output: [[0,4], [1,3], [1,4], [2,2], [3,0], [3,1], [4,0]]

Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
'''

class Solution:
    '''
    INTUITION: 
    Start from ocean boundary/ocean line and trace the sources of rain water upstream. 
    Assume, you are at the ocean line and it's raining, can you follow where the rain water is coming.
    '''
    
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        to_pacific, to_atlantic = set(), set()

        # iterate over the top row and bottom row 
        for col in range(cols):
            self.flows_to_ocean(heights, 0, col, 0, to_pacific)
            self.flows_to_ocean(heights, rows - 1, col, 0, to_atlantic)

        # iterate over the left most column and right most column
        for row in range(rows):
            self.flows_to_ocean(heights, row, 0, 0, to_pacific)
            self.flows_to_ocean(heights, row, cols - 1, 0, to_atlantic)

        return list(to_pacific & to_atlantic)
    
    def flows_to_ocean(self, heights: list, row: int, col: int, prev_height: int, visited: set) -> None:
        n, m = len(heights), len(heights[0])
        outside_bound = not((0 <= row < n) and (0 <= col < m))

        if outside_bound or (row, col) in visited or heights[row][col] < prev_height:
            return

        # Add this cell to the visited(flows_to_ocean) list
        visited.add((row, col))
        for (dx, dy) in self.directions:
            self.flows_to_ocean(heights, row + dx, col + dy, heights[row][col], visited)

    @property
    def directions(self):
        return [(0, -1), (0, 1), (-1, 0), (1, 0)]
