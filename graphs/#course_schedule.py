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


def canFinish(numCourses, prerequisites):
    pre_map = {i: [] for i in range(numCourses)}

    for course, pre in prerequisites:
        pre_map[course].append(pre)

    visited = set()

    for course in range(numCourses):
        if not dfs(course, pre_map, visited):
            return False

    return True


def dfs(course, pre_map, visited):
    if course in visited:
        return False

    if pre_map[course] == []:
        return True

    visited.add(course)

    for pre in pre_map[course]:
        if not dfs(pre):
            return False

    visited.remove(course)
    pre_map[course] = []
    return True
