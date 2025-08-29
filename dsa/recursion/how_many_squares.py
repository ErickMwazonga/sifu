# https://www.youtube.com/watch?v=kuh9iRYoN9A

def nos_of_squares(N: int) -> int:
    if N == 1:
        return 1
    return nos_of_squares(N-1) + N ** 2

assert nos_of_squares(2) == 5
assert nos_of_squares(3) == 14
assert nos_of_squares(4) == 30
assert nos_of_squares(5) == 55