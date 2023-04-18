from heapq import heappush, heappop
from collections import defaultdict

INF: float = float('inf')


def digikstra(graph: dict[str, dict[str, int]], start: str) -> dict[str, int]:
    '''Write a function to find the shortest path from start to all other nodes in the graph.'''

    visited_nodes: set[str] = set()
    distances: dict[str, int] = {start: 0}
    paths: dict[str, list[str]] = defaultdict(list)
    # Distance starts because it will used for comparison in heaps
    priority_queue: list[tuple[str, int]] = [(0, start)]

    paths[start].append(start)

    while priority_queue:
        curr_distance, curr_node = heappop(priority_queue)
        neighbours = graph[curr_node]

        if curr_node in visited_nodes:
            continue

        # Visit node
        visited_nodes.add(curr_node)

        # consider all neighbours
        for (node, distance) in neighbours.items():
            new_distance = curr_distance + distance

            if node not in distances or new_distance < distances[node]:
                distances[node] = new_distance
                paths[node] = paths[curr_node] + [node]

            # prev_distance = distances.get(node, INF)
            # distances[node] = min(new_distance, prev_distance)

            # print(f'{curr_node}: {node} -> {distances[node]}')
            heappush(priority_queue, (new_distance, node))

    print(distances)
    print(dict(paths))

    return distances


def digikstra2(graph: dict[str, dict[str, int]], start: str, end: str) -> dict[str, int]:
    pass


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 2, 'E': 3, 'C': 3},
    'C': {'B': 1, 'D': 4, 'E': 5},
    'D': {},
    'E': {'D': 1}
}

print(digikstra(graph, 'A'))
