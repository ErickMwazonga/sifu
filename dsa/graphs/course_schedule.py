'''
207. Course Schedule
Link: https://leetcode.com/problems/course-schedule/
Resource: https://www.youtube.com/watch?v=EgI5nU9etnU&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=2

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] 
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1, 0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible
'''

from collections import defaultdict

class Solution:
    def isACycle(self, node, visited, graph):
        has_cycle = False
        visited[node] = 1
        for child in graph[node]:
            if not visited[child]:
                has_cycle = self.isACycle(child, visited, graph)
            elif visited[child] == 1:
                has_cycle = True
                
        visited[node] = 2
        return has_cycle

    def build_graph(self, prerequisites):
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        return graph

    def canFinish(self, numCourses, prerequisites):
        graph = self.build_graph(prerequisites)
        visited = [0] * numCourses

        for i in range(numCourses):
            if not visited[i]:
                if self.isACycle(i, visited, graph):
                    return False
        return True