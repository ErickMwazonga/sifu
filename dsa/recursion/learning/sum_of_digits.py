'''
Given a positive integer n, create a recursive function that returns the sum of its digits
425 -> 11
'''


def sumOfDigits(n, sum=0):
    if n <= 0:
        return sum
    else:
        n, rem = divmod(n, 10)
        return sumOfDigits(n, sum + rem)


def sumOfDigits_v2(n):
    if n < 10:
        return n
    else:
        n, rem = divmod(n, 10)
        return rem + sumOfDigits_v2(n)


def sumOfDigts_v3(n):
    if n < 0:  # Negative numbers
        return sumOfDigts_v3(-n)
    elif n < 10:
        return n
    else:
        return (n % 10) + sumOfDigts_v3(n // 10)


def sumOfDigts_v4(n, acc=0):
    if n < 0:
        return sumOfDigits(-n)
    elif n < 10:
        return n + acc
    else:
        return sumOfDigits(n // 10, acc + n % 10)
