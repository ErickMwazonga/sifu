'''
https://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/'
https://medium.com/@rrfd/explaining-the-josephus-algorithm-11d0c02e7212
'''


def josephus(n, k):
    if n == 1:
        return 1
    else:
        return ((josephus(n-1, k) + k-1) % n) + 1


def josephus2(n, k):
    r = 0
    i = 1
    while i <= n:
        r = (r + k) % i
        i += 1
    return r + 1
