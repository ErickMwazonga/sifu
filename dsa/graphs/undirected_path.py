'''
undirected path
https://structy.net/problems/undirected-path

Write a function, undirectedPath, that takes in an array of edges for an undirected graph and two nodes (nodeA, nodeB). 
The function should return a boolean indicating whether or not there exists a path between nodeA and nodeB.

Example:
edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
]
'''


from collections import defaultdict


def undirected_path(edges, nodeA, nodeB):
    graph = build_graph(edges)
    return has_path(graph, nodeA, nodeB, set())


def build_graph(edges):
    graph = defaultdict(list)

    for edge in edges:
        a, b = edge

        graph[a].append(b)
        graph[b].append(a)

    return graph


def has_path(graph, src, dst, visited):
    if src == dst:
        return True

    if src in visited:
        return False

    visited.add(src)

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited) == True:
            return True

    return False
