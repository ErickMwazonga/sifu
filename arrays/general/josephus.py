'''
https://www.codespeedy.com/josephus-problem-and-recursive-solution-in-python/
https://medium.com/@rrfd/explaining-the-josephus-algorithm-11d0c02e7212

In Josephus problem, n people are standing in a circle waiting to be executed and in every iteration,
we kill the kth person and remove that person from the circle.
'''


def josephus_problem(n, k):
    if n == 1:
        return 0

    return 1 + (josephus_problem(n-1, k) + k-1) % n
