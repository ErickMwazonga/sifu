'''
611. Knight Shortest Path [LintCode]
https://mrleonhuang.gitbooks.io/lintcode/content/dynamic-programming/knight-shortest-path.html

Given a knight in a chessboard (a binary matrix with 0 as empty a 1 as barrier) with a sourceposition,
find the shortest path to a destinationposition, return the length of the route.

Return -1 if knight can not reached.

Notice
source and destination must be empty.
Knight can not enter the barrier.

Clarification
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)

Example
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
source = [2, 0] destination = [2, 2] return 2

[[0, 1, 0],
 [0, 0, 0],
 [0, 0, 0]]
source = [2, 0] destination = [2, 2] return 6

[[0, 1, 0],
 [0, 0, 1],
 [0, 0, 0]]
source = [2, 0] destination = [2, 2] return -1
'''

from collections import deque


class Solution:

    def get_knight_directions(self):
        return [
            (1, 2), (1, -2),
            (-1, 2), (-1, -2),
            (2, 1), (2, -1),
            (-2, 1), (-2, -1)
        ]

    def is_valid_move(self, board, x, y):
        N, M = len(board), len(board[0])

        if not ((0 <= x < N) and (0 <= y < M)):
            return False
        if board[x][y] == 1:
            return False

        return True


    def knight_shortest_path(self, board, start, end):
        N, M = len(board), len(board[0])

        moves = self.get_knight_directions()
        queue = deque([(start, 0)])
        visited = set([f'{start[0]}{start[1]}'])

        while queue:
            curr_position, distance = queue.popleft()
            x, y = curr_position

            if curr_position == end:
                return distance

            for move in moves:
                new_x, new_y = x + move[0], y + move[1]
                key = f'{new_x}{new_y}'

                if key in visited:
                    continue

                if not self.is_valid_move(board, x, y):
                    continue

                queue.append(((new_x, new_y), distance + 1))
                visited.add(key)

        return -1


soln = Solution()

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
source, destination = (2, 0), (2, 2)
assert soln.knight_shortest_path(board, source, destination) == 2

board_1 = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 0, 0]
]
source, destination = (2, 0), (2, 2)
assert soln.knight_shortest_path(board_1, source, destination) == 6

board_2 = [
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0]
]
source, destination = (2, 0), (2, 2)
assert soln.knight_shortest_path(board_2, source, destination) == -1
