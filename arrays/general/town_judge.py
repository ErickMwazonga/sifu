'''
997. Find the Town Judge
In a town, there are N people labelled from 1 to N. 
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b]
representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Input: N = 2, trust = [[1,2]]
Output: 2

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
'''


def findJudge(N: int, trust: List[List[int]]) -> int:
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
