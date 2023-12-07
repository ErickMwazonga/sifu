from collections import deque


class Solution:

    def get_possible_directions(self):
        return [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def is_valid_move(self, grid, x, y):
        N, M = len(grid), len(grid[0])

        if not ((0 <= x < N) and (0 <= y < M)):
            return False
        if grid[x][y] == 0:
            return False

        return True


    def dungeon_master(self, grid, start, end):
        N, M = len(grid), len(grid[0])
        directions = self.get_possible_directions()

        queue = deque([(start, 0)])
        visited = set([start])

        while queue:
            current_node, distance = queue.popleft()
            x, y = current_node

            if current_node == end:
                return distance

            for direction in directions:
                new_x, new_y = x + direction[0], y + direction[1]
                new_node = (new_x, new_y)

                if new_node in visited:
                    continue

                if not self.is_valid_move(grid, x, y):
                    continue

                queue.append((new_node, distance + 1))
                visited.add(direction)

        return -1


soln = Solution()

grid = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

start = (0, 0)
end = (4, 4)

assert soln.dungeon_master(grid, start, end) == 12
