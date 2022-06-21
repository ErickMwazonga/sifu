'''
shortest path
https://structy.net/problems/shortest-path

Write a function, shortestPath, that takes in an array of edges for an undirected graph and two nodes (nodeA, nodeB).
The function should return the length of the shortest path between A and B.
Consider the length as the number of edges in the path, not the number of nodes.
If there is no path between A and B, then return -1.

Example 1
const edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
];
shortestPath(edges, 'w', 'z') -> 2

Example 2
const edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
];
shortestPath(edges, 'a', 'e') -> 3
'''


def shortestPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)

    visited = set(nodeA)
    queue = [[nodeA, 0]]

    while queue:
        node, distance = queue.pop(0)

        if node == nodeB:
            return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.push([neighbor, distance + 1])

    return -1


def buildGraph(edges):
    graph = {}

    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph
