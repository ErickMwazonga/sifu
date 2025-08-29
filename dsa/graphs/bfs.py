'''
Graph breadth first search
Given an undirected graph of integers graph, represented by an adjacency list,
and an integer root, create a function that prints its values in breadth first search,
by considering the vertex whose value is root as the arbitrary node.

Example 1:
Input: graph = {
    5 : [8, 1, 12],
    8 : [5, 12, 14, 4],
    12 : [5, 8, 14],
    14 : [8, 12, 4],
    4 : [8, 14],
    1 : [5, 7],
    7 : [1, 16],
    16 : [7]
}
root = 5
Output: 5 8 1 12 14 4 7 16
'''


def bfs(graph, root):
    res, visited, queue = [], set([root]), [root]

    while queue:
        curr = queue.pop(0)
        res.append(curr)

        for neighbor in graph[curr]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return res

class Graph_BFS:
    '''Time complexity: O(|V|+|E|), Space complexity: O(|V|)'''

    def __init__(self, adjList={}):
        self.adjList = adjList

    def bfs(self, graph, root):
        queue = [root]
        visited = {root}

        while queue:
            vertex = queue.pop(0)

            for neighbor in graph.adjList[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def bfs_improved(self, graph, root):
        queue = [root]
        visited = {root}
        i = 0

        while i < len(queue):
            vertex = queue[i]
            i += 1

            for neighbor in graph.adjList[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

graph = {
    5: [8, 1, 12],
    8: [5, 12, 14, 4],
    12: [5, 8, 14],
    14: [8, 12, 4],
    4: [8, 14],
    1: [5, 7],
    7: [1, 16],
    16: [7]
}

assert bfs(graph, 5) == [5, 8, 1, 12, 14, 4, 7, 16]


def bfs_x(graph, root):
    visited, queue, res = set(), [root], []

    while queue:
        curr_node = queue.pop(0)

        if curr_node in visited:
            continue

        visited.add(curr_node)
        res.append(curr_node)

        for neighbour in graph[curr_node]:
            if neighbour not in visited:
                queue.append(neighbour)

    # Cannot return set because it is not ordered
    return res


print(bfs_x(graph, 5))
