'''
733. Flood Fill
https://leetcode.com/problems/flood-fill/

Wikipedia: https://en.wikipedia.org/wiki/Flood_fill
Video Explanation: https://www.youtube.com/watch?v=VuiXOc81UDM

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color.
You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally
to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels (also with the same color), and so on.
Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel),
all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
Input: image = [[0,0,0], [0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0], [0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
'''

# DFS approach:

class FLOOD_FILL_DFS:

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old_color, new_color = image[sr][sc], color
        if old_color == new_color:
            return image

        self.dfs(image, sr, sc, old_color, new_color)
        return image

    def dfs(self, grid, i, j, old_color, new_color):
        n, m = len(grid), len(grid[0])

        inbound = (0 <= i < n) and (0 <= j < m)
        # if not inbound or image[sr][sc] != old_color or image[sr][sc] == new_color: 
        if not inbound or grid[i][j] != old_color:
            return

        grid[i][j] = new_color

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            self.dfs(grid, i + dx, j + dy, old_color, new_color)

    
 
# BFS approach:
from collections import deque


class FLOOD_FILL_BFS:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old_color, new_color = image[sr][sc], color
        if old_color == new_color:
            return image

        self.bfs(image, sr, sc, old_color, new_color)
        return image

    def bfs(self, image, row, col, old_color, new_color):
        n, m = len(image), len(image[0])
        
        queue = deque([(row, col)])

        while queue:
            # Get next neighbour
            i, j = queue.popleft()

            # Change the color of the current pixel
            image[i][j] = new_color

            # Check the four neighbors
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                
                inbound = (0 <= i < n) and (0 <= j < m)
                if inbound and image[ni][nj] == old_color:
                    queue.append((ni, nj))
            
