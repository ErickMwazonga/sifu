'''
997. Find the Town Judge
Link: https://leetcode.com/problems/find-the-town-judge/

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
Input: N = 3, trust = [[1, 3], [2, 3]]
Output: 3

Input: N = 3, trust = [[1, 3], [2, 3], [3, 1]]
Output: -1

Input: N = 4, trust = [[1,3], [1,4], [2,3], [2,4], [4,3]]
Output: 3
'''


from collections import defaultdict


def findJudge(N, trusts):
    count = [0] * (N + 1)

    for i, j in trusts:
        count[i] -= 1
        count[j] += 1

    for i in range(1, N + 1):
        if count[i] == N - 1:
            return i

    return -1


def find_judge_v0(N: int, trust: list[list[int]]) -> int:
    '''Inspired by https://www.youtube.com/watch?v=ZUP_tIs4VaE&t=419s'''

    if N == 1 and not trust:
        return 1

    if not trust:
        return -1

    if N == 1:
        return trust[0][1]

    mapping = [[0, 0] for _ in range(N+1)]

    for person in trust:
        trusting, trusted_by = person

        mapping[trusting][0] += 1
        mapping[trusted_by][1] += 1

    for i in range(len(mapping)):
        trusting, trusted_by = mapping[i]

        if trusting == 0 and trusted_by == N-1:
            return i

    return -1


def find_judge_v2(N, trusts) -> int:
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


assert find_judge(2, [[1, 2]]) == 2
assert find_judge(3, [[1, 3], [2, 3], [3, 1]]) == -1
assert find_judge(3, [[1, 2], [2, 3]]) == -1
assert find_judge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3

assert find_judge_v2(2, [[1, 2]]) == 2
assert find_judge_v2(3, [[1, 3], [2, 3], [3, 1]]) == -1
assert find_judge_v2(3, [[1, 2], [2, 3]]) == -1
assert find_judge_v2(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3
