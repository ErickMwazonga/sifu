'''
has path
https://structy.net/problems/has-path

Write a function, hasPath, that takes in an object representing the adjacency
list of a directed acyclic graph and two nodes (src, dst).
The function should return a boolean indicating whether or not
there exists a directed path between the source and destination nodes.

test_00:
const graph = {
  f: ['g', 'i'],
  g: ['h'],
  h: [],
  i: ['g', 'k'],
  j: ['i'],
  k: []
};
hasPath(graph, 'f', 'k'); // true
'''


# DFS
def hasPath(graph, src, dst):
    '''
    n = number of nodes, e = number edges
    Time: O(e), Space: O(n)
    '''

    if src == dst:
        return True

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst) == True:
            return True

    return False


# BFS
def hasPath(graph, src, dst):
    '''
    n = number of nodes, e = number edges
    Time: O(e), Space: O(n)
    '''

    queue = [src]

    while (queue.length):
        current = queue.pop(0)

        if (current == dst):
            return True

        for neighbor in graph[current]:
            queue.push(neighbor)

    return False
