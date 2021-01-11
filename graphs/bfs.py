'''
Graph breadth first search
Given an undirected graph of integers graph, represented by an adjacency list,
and an integer root, create a function that prints its values in breadth first search,
by considering the vertex whose value is root as the arbitrary node.

Example 1:
Input: graph = {
    "5" : [8, 1, 12],
    "8" : [5, 12, 14, 4],
    "12" : [5, 8, 14],
    "14" : [8, 12, 4],
    "4" : [8, 14],
    "1" : [5, 7],
    "7" : [1, 16],
    "16" : [7]
}
root = 5
Output: 5 8 1 12 14 4 7 16

'''

class Graph:
    '''
    Time complexity: O(|V|+|E|)
    Space complexity: O(|V|)
    '''
    
    def __init__(self, adjList = {}):
        # the adjacency list is of type Dict[int,List[int]]
        self.adjList = adjList

    def bfs(graph, root):
        queue = [root]
        visited = {root}

        while queue:
            vertex = queue.pop(0)
            print(vertex)

            for neighbor in graph.adjList[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def bfs_improved(graph, root):
        queue = [root]
        visited = {root}
        i = 0

        while i < len(queue):
            vertex = queue[i]
            i += 1
            print(vertex)

            for neighbor in graph.adjList[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)