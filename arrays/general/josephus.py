'''
https://www.codespeedy.com/josephus-problem-and-recursive-solution-in-python/
https://medium.com/@rrfd/explaining-the-josephus-algorithm-11d0c02e7212

In Josephus problem, n people are standing in a circle waiting to be executed and in every iteration,
we kill the kth person and remove that person from the circle.
'''


def josephus(n, skip):
    lst = list(range(1, n + 1))
    skip = skip - 1  # list starts with 0 index
    idx = 0

    while n > 0:
        idx = (idx + skip) % n  # hash index to every 3rd
        lst.pop(idx)
        n -= 1


def josephus_v2(n, skip):
    skip = skip - 1  # list starts with 0 index
    idx = 0

    lst = list(range(1, n+1))
    len_list = len(lst)

    killed_in_order = []

    while len_list > 0:
        idx = (idx + skip) % len_list  # hash index to every 3rd
        victim = lst.pop(idx)
        killed_in_order.append(victim)
        len_list -= 1

    return killed_in_order


assert josephus_v2(9, 3) == [3, 6, 9, 4, 8, 5, 2, 7, 1]
