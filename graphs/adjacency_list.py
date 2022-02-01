# Adjacency List representation in Python

from collections import defaultdict


class Node:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self):
        self.adjList = {}

    def add_node(self, node):
        if node not in self.adjList:
            self.adjList[node] = []

    def add_edge(self, s, d):
        if s not in self.adjList:
            self.adjList[s] = [d]
        else:
            self.adjList[s].append(d)

    def print_graph(self):
        for k, v in self.adjList.items():
            print(f'{k} -> {v}')


if __name__ == "__main__":

    # Create graph and edges
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_graph()
