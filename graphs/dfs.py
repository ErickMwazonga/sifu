'''
Graph depth first search
Given an undirected graph of integers graph, represented by an adjacency list,
and an integer root, create a function that prints its values in depth first search,
by considering the vertex whose value is root as the arbitrary node.

Example 1:
graph = {
    5 : [8, 1, 12],
    8 : [5, 12, 14, 4],
    12 : [5, 8, 14],
    14 : [8, 12, 4],
    4 : [8, 14],
    1 : [5, 7],
    7 : [1, 16],
    16 : [7]
},
root = 5
Output: 5 8 12 14 4 1 7 16
'''


class DFSTraversal:
    '''Time complexity: O(|V|+|E|), Space complexity: O(|V|)'''

    def __init__(self, graph={}):
        self.adjList = graph  # of type Dict[int,list[int]]

    def traverse(self, root):
        res, visited = [], set()
        self.dfs(root, visited, res)

        # a set is unordered hence cannot be used to return the results
        return res

    def dfs(self, root, visited, res):
        if root in visited:
            return

        visited.add(root)
        res.append(root)

        for neighbour in self.adjList[root]:
            self.dfs(neighbour, visited, res)

    def dfs2(self, node, visited):
        if node in visited:
            return

        visited.append(node)
        for k in graph[node]:
            self.dfs(self.adjList, k, visited)


class DFSTraversal_V2:
    def __init__(self, graph):
        self.graph = graph

    def dfs(self, root):
        res, visited = [], set([root])
        stack = [root]

        while stack:
            curr = stack.pop()
            res.append(curr)

            for neighbor in reversed(self.graph[curr]):
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

        return res


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
soln = DFSTraversal(graph)
print(soln.traverse(root=5))
# assert soln.traverse(graph, 5) ==  [1, 4, 5, 7, 8, 12, 14, 16]

soln = DFSTraversal_V2(graph)
print(soln.dfs(root=5))
# assert soln.dfs(graph, 5) == [5, 8, 14, 4, 1, 7, 16, 12] # [5, 8, 14, 4, 1, 7, 16, 12]
