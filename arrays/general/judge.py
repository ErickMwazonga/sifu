'''
997. Find the Town Judge
https://leetcode.com/problems/find-the-town-judge/

In a town, there are N people labelled from 1 to N. 
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b]
representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge. 
Otherwise, return -1.

Examples
Input: N = 2, trust = [[1,2]]
Output: 2

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
'''

from collections import defaultdict


def find_judge(N, trusts):
    trustees = [[] for _ in range(N)]
    trusted = [[] for _ in range(N)]

    for i in range(1, N+1):
        trust, trusted = trusts[i]

        trustees[i] = trustees[i].append(trusted)
        trusted[i] = trusted[i].append(trusted)

    for i in range(1, N+1):
        if len(trustees[i]) == 0 and trusted[i] == N-1:
            return i

    return -1


def findJudge(N, trusts):
    trusting = defaultdict(list)
    trusted_by = defaultdict(int)

    for trust in trusts:
        person, trusted = trust

        trusting[person].append(trusted)
        trusted_by[trusted] += 1

    for i in range(1, N+1):
        if len(trusting[i]) == 0 and trusted_by[i] == N-1:
            return i

    return -1


'''
[[1,3], [2,3], [3,1]]

    1,    2,    3
T   3     3     1 (0)
TS  3           1,2 (N-1)

[[1,3],[1,4],[2,3],[2,4],[4,3]]

        1    2    3    4
T       3,4  3,4       3
TS               1,2,4  1,2

'''
