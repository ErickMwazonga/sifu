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


class DFS:
    def hasPath(self, graph, src, dest):
        '''
        n = number of nodes, e = number edges
        Time: O(e), Space: O(n)
        '''

        if src == dest:
            return True

        for neighbor in graph[src]:
            if self.hasPath(graph, neighbor, dest):
                return True

        return False

    def check_path(self, graph, src, dest):
        # cannot pass boolean to a recursive function - NOTEs
        has_path = [False]
        self.hasPath_v2(graph, src, dest, has_path)

        return has_path[0]

    def hasPath_v2(self, graph, src, dest, has_path):
        print(src, dest, src == dest)

        if src == dest:
            print('EXECUTED')
            has_path[0] = True
            return

        if not graph[src]:
            return

        for neighbor in graph[src]:
            self.hasPath_v2(graph, neighbor, dest, has_path)

        return False


class BFS:
    def hasPath_v2(self, graph, src, dest):
        '''
        n = number of nodes, e = number edges
        Time: O(e), Space: O(n)
        '''

        queue = [src]

        while len(queue):
            current = queue.pop(0)

            if current == dest:
                return True

            for neighbor in graph[current]:
                queue.push(neighbor)

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
