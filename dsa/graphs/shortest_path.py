'''
shortest path
https://structy.net/problems/shortest-path

Write a function, shortestPath, that takes in an array of edges for an undirected graph and two nodes (nodeA, nodeB).
The function should return the length of the shortest path between A and B.
Consider the length as the number of edges in the path, not the number of nodes.
If there is no path between A and B, then return -1.

Example 1
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]
shortestPath(edges, 'w', 'z') -> 2

Example 2
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]
shortestPath(edges, 'a', 'e') -> 3
'''

from collections import defaultdict, deque


class Solution:

    def build_graph(self, edges):
        graph = defaultdict(list)
        for source, dest in edges:
            graph[source].append(dest)
            graph[dest].append(source)
        return graph

    def shortestPath(self, edges, nodeA, nodeB):
        graph = self.build_graph(edges)  # graph

        queue = deque([(nodeA, 0)])
        visited = set(nodeA)

        while queue:
            curr_node, distance = queue.popleft()

            if curr_node == nodeB:
                return distance

            for neighbor in graph[curr_node]:
                if neighbor in visited:
                    continue

                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

        return -1


edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

soln = Solution()
assert soln.shortestPath(edges, 'a', 'e') == 3
