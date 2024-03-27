'''
787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are n cities connected by some number of flights. 
You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there 
is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.

Example 1:
Input: n = 4, flights = [[0, 1, 100],  [1, 2, 100],  [2, 0, 100],  [1, 3, 600],  [2, 3, 200]], src = 0, dst = 3, k = 1
Output: 700

Explanation:
    The graph is shown above.
    The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
    Note that the path through cities [0, 1, 2, 3] is cheaper but is invalid because it uses 2 stops.

Example 2:
Input: n = 3, flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0, dst = 2, k = 1
Output: 200

Example 3:
Input: n = 3, flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0, dst = 2, k = 0
Output: 500
'''

from collections import defaultdict, deque
from typing import List


class Solution_BFS:
    def build_graph(self, flights: List[List[int]]) -> defaultdict:
        graph = defaultdict(list)
        for _from, _to, to_dist in flights:
            graph[_from].append((_to, to_dist))
        return graph

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = self.build_graph(flights)

        # Initialize distances to all nodes as infinity except the source node which is 0
        distances = [float("inf")] * n
        distances[src] = 0

        # Initialize the queue for BFS traversal
        queue = deque([(src, 0, 0)])  # (source node, covered distance, stops)

        while queue:
            curr, covered_dist, stops = queue.popleft()

            # If the number of stops exceeds the limit, skip
            if stops > k:
                continue

            for _to, to_dist in graph[curr]:
                new_distance = covered_dist + to_dist

                # If the new distance is less than the current distance to the neighbor,
                # update the distance and add the neighbor to the queue for further exploration
                if new_distance < distances[_to]:
                    distances[_to] = new_distance
                    queue.append((_to, new_distance, stops + 1))

        # Return the shortest distance to the destination node if it's reachable,
        # otherwise return -1
        return distances[dst] if distances[dst] != float("inf") else -1


class Solution_DFS:
    '''DFS'''

    def build_graph(self, flights):
        graph = defaultdict(list)

        for _from, to, price in flights:
            graph[_from].append((to, price))

        return graph

    def findCheapestPrice(self, n: int, flights, src: int, dest: int, K: int) -> int:
        graph = self.build_graph(flights)

        memo = {}
        res = self.dfs(src, dest, K, memo, graph, stops=0)

        return res if res != float('inf') else -1

    def dfs(self, node, dest, k, memo, graph, stops):
        if node == dest:
            return 0

        if k < 0:
            return float('inf')

        if (node, k) in memo:
            return memo[(node, k)]

        res = float('inf')
        for nei, price in graph[node]:
            upto_this_node = self.dfs(nei, dest, k-1, memo, graph, stops)
            res = min(upto_this_node + price, res)

        memo[(node, k)] = res
        return memo[(node, k)]
