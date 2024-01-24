'''
Kill Process (leetcode 582)
https://leetcode.ca/2017-07-04-582-Kill-Process/

Given n processes, each process has a unique PID (process id) and its PPID (parent process id).

Each process only has one parent process, but may have one or more children processes.
This is just like a tree structure. Only one process has PPID that is 0,
which means this process has no parent process.
All the PIDs will be distinct positive integers.

We use two list of integers to represent a list of processes,
where the first list contains PID for each process and the second list contains the corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill,
return a list of PIDs of processes that will be killed in the end.
You should assume that when a process is killed, all its children processes will be killed.
No order is required for the final answer.

Example 1:
Input:
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation:
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.


INTUITION

HashMap + DFS in Python
we can use a hashmap which stores a particular process value and the list of its direct children.
And then treat it as a tree traversal problem.
'''

from collections import defaultdict


class Solution:

    def __init__(self):
        self.mapping = defaultdict(list)

    def kill_process(self, pids, ppids, kill):
        matches = zip(ppids, pids)

        for ppid, pid in matches:
            self.mapping[ppid].append(pid)

        visited = set()
        self.dfs(kill, visited)
        return list(visited)

    def dfs(self, curr_node, visited):
        if curr_node in visited:
            return

        visited.add(curr_node)

        for child in self.mapping[curr_node]:
            self.dfs(child, visited)


soln = Solution()

# Example usages
pids = [1, 2, 3, 4, 5]
ppids = [0, 1, 1, 2, 2]

pids =  [1, 3, 10, 5]
ppids = [3, 0, 5, 3]
print(soln.kill_process(pids, ppids, 5))
