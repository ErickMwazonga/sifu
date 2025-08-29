'''
has path
https://structy.net/problems/has-path

Write a function, hasPath, that takes in an object representing the adjacency
list of a directed acyclic graph and two nodes (src, dest).
The function should return a boolean indicating whether or not
there exists a directed path between the source and destination nodes.

test_00:
graph = {
  f: ['g', 'i'],
  g: ['h'],
  h: [],
  i: ['g', 'k'],
  j: ['i'],
  k: []
}
hasPath(graph, 'f', 'k') # True
'''

from collections import deque

class DFS:

    def hasPath(graph, source, dest, visited):
        if source == dest:
            return True
        
        visited.add(source)
        for neighbor in graph[source]:
            if neighbor not in visited:
                if dfs(neighbor, neighbor, dest, visited):
                    return True
        return False


    def check_path(self, graph, src, dest):
        visited = set()
        return self.hasPath_v2(graph, src, dest, visited)



class BFS:
    def hasPath_v2(self, graph, src, dest):
        '''
        n = number of nodes, e = number edges
        Time: O(e), Space: O(n)
        '''
        visited = set()
        queue = deque([src])
        
        while queue:
            curr = queue.popleft()
            if curr == dest:
                return True
            
            visited.add(curr)
            for child in graph.get(curr, []):
                if child not in visited:
                    queue.append(child)
        return False

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

dfs = DFS()
print(dfs.check_path(graph, 'f', 'k'))
# assert dfs.hasPath(graph, 'f', 'k') == True
# assert dfs.hasPath(graph, 'h', 'k') == False
