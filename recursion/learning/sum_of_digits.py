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


def sumOfDigits(n):
    if n < 10:
        return n
    else:
        n, rem = divmod(n, 10)
        return rem + sumOfDigits(n)

# non-tail recursive:


def sumOfDigts(n):
    if n < 0:  # Negative numbers
        return sumOfDigts(-n)
    elif n < 10:
        return n
    else:
        return (n % 10) + sumOfDigts(n // 10)

# tail recursive:


def sumOfDigts(n, acc=0):
    if n < 0:
        return sumOfDigits(-n)
    elif n < 10:
        return n+acc
    else:
        return sumOfDigits(n//10, acc+n % 10)
