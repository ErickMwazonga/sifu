'''
D. Distance in Tree
https://codeforces.com/problemset/problem/161/D

A tree is a connected graph that doesn't contain any cycles.
The distance between two vertices of a tree is the length (in edges) of the shortest path between these vertices.
You are given a tree with n vertices and a positive number k. Find the number of distinct pairs of the vertices which have a distance of exactly k between them.
Note that pairs (v, u) and (u, v) are considered to be the same pair.

Input
The first line contains two integers n and k (1 ≤ n ≤ 50000, 1 ≤ k ≤ 500) — the number of vertices and the required distance between the vertices.
Next n - 1 lines describe the edges as "ai bi" (without the quotes) (1 ≤ ai, bi ≤ n, ai ≠ bi), where ai and bi are the vertices connected by the i-th edge. All given edges are different.

Output
Print a single integer — the number of distinct pairs of the tree's vertices which have a distance of exactly k between them.

Examples
inputCopy
5 2
1 2
2 3
3 4
2 5
outputCopy
4
inputCopy
5 3
1 2
2 3
3 4
4 5
outputCopy
2
Note
In the first sample the pairs of vertexes at distance 2 from each other are (1, 3), (1, 5), (3, 5) and (2, 4).
'''