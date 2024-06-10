'''
Walls and Gates
Link: https://leetcode.com/problems/walls-and-gates
Resource: https://www.youtube.com/watch?v=e69C6xhiSQE

You are given a m x n 2D grid initialized with these three possible values.
-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF
as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate.

If it is impossible to reach a gate, it should be filled with INF.

Example:
INF  -1  0  INF             3  -1   0   1
INF INF INF  -1   -->       2   2   1  -1
INF  -1 INF  -1             1  -1   2  -1
  0  -1 INF INF             0  -1   3   4
'''

from collections import deque


class Solution_DFS:
    '''DFS - Time: O(NM)^2, Space: O(NM)'''

    def walls_and_gates(self, rooms):
        if not rooms:
            return rooms

        n, m = len(rooms), len(rooms[0])
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, dist=0)

    def dfs(self, rooms, i, j, dist):
        n, m = len(rooms), len(rooms[0])
        out_bounds = i < 0 or i >= n or j < 0 or j >= m

        if out_bounds or rooms[i][j] == -1 or rooms[i][j] < dist:
            return

        rooms[i][j] = dist  # update
        self.dfs(rooms, i - 1, j, dist + 1)
        self.dfs(rooms, i + 1, j, dist + 1)
        self.dfs(rooms, i, j - 1, dist + 1)
        self.dfs(rooms, i, j + 1, dist + 1)


    def dfs_v2(self, rooms, i, j, dist):
        n, m = len(rooms), len(rooms[i])
        out_bounds = i < 0 or i >= n or j < 0 or j >= m
        if out_bounds or rooms[i][j] == -1 or rooms[i][j] < dist:
            return

        rooms[i][j] = 0  # SINK

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            self.dfs(rooms, i + dx, j + dy, dist + 1)


class Solution_BFS:
    @property
    def directions(self):
        return [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    def wallsAndGates(self, rooms):
        queue = deque([])
        for i in range(0, len(rooms)):
            for j in range(0, len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            i, j = queue.popleft()
            for di, dj in self.directions:
                x, y = i + di, j + dj
                inbounds = 0 <= x < len(rooms) and 0 <= y < len(rooms[0])
                if inbounds and rooms[x][y] == float('inf'):
                    rooms[x][y] = rooms[i][j] + 1
                    queue.append((x, y))
