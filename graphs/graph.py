from collections import defaultdict

class Graph:

    def _init_(self, edges=None):
        self.graph = defaultdict(list)

        if edges:
            for u, v in edges:
                self.add_edge(u, v)

    def add_edge(self, u, v):
        '''Add edge in a directed graph'''
        self.graph[u].append(v)

    def show(self):
        '''Show each vertex with all its edges'''
        for k, v in self.graph.items():
            for w in v:
                print(f'{k} --> {w}')

    def dfs(self, v):
        '''Perform a DFS on node v as starting point'''
        # Have a visited set to handle case of cycles
        visited = set()

        def traverse(v)
            if v not in visited:
                print(f'DFS Visited vertex {v}')
                
                visited.add(v)
                for other in self.graph[v]:
                    traverse(other)

        traverse(v)
        return visited

    def bfs(self, v):
        '''Perform a breath first traversal from node v'''
        queue = [v]
        visited = set()

        while(queue):
            node = queue.pop(0)

            if node not in visited:
                print(f'BFS Visited vertex {node}')
                visited.add(node)

                for other in self.graph[node]:
                    queue.append(other)
                    
        return visited


edges = [
    ('A', 'B'),
    ('A', 'E'),
    ('A', 'H'),
    ('A', 'K'),
    ('B', 'C'),
    ('C', 'D'),
    ('E', 'F'),
    ('F', 'G'),
    ('H', 'I'),
    ('I', 'J'),
    ('K', 'L'),
    ('L', 'M')
]


graph = Graph(edges=edges)

# graph.dfs('A')
graph.bfs('A')`