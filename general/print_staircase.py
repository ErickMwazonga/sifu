'''
Staircase detail

This is a staircase of size n = 4:
   #
  ##
 ###
####
Its base and height are both equal to n. It is drawn using # symbols and spaces.
The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.
'''


def staircase(n):
    for i in range(1, n+1):
        _row = (' ' * (n-i)) + ('#' * i)
        print(_row)


def staircase_v2(n):
    for i in range(n):
        for j in range(n-1, -1, -1):
            if i < j:
                print(' ', end='')
            else:
                print('#', end='')
        print()
