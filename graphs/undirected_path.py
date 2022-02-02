'''
undirected path
https://structy.net/problems/undirected-path

Write a function, undirectedPath, that takes in an array of edges for an undirected graph and two nodes (nodeA, nodeB). 
The function should return a boolean indicating whether or not there exists a path between nodeA and nodeB.

test_00:
const edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
]
'''


def undirectedPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB, set())


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


def hasPath(graph, src, dst, visited):
    if src == dst:
        return True

    if src in visited:
        return False

    visited.add(src)

    for neighbor in graph[src]:
        if (hasPath(graph, neighbor, dst, visited) == True):
            return True

    return False
