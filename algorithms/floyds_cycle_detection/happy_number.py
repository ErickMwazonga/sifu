'''
202. Happy Number
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number n is "happy".
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 
Input: 19 -> true
Explanation: 
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1
'''

def isHappy(n: int) -> bool:
	slow = squared(n)
	fast = squared(squared(n))

	while slow != fast:
		slow = squared(slow)
		fast = squared(squared(fast))

	return slow == 1

def squared(n):
	return sum([int(x) ** 2 for x in str(n)])

def squared2(n):
	result = 0

	while n > 0:
		n, last = divmod(n, 10)
		result += last * last

	return result

def isHappy(n):
	seen = { n }

	while (n):
		n = squared(n)

		if n == 1:
			return True
		elif n in seen:
            return False
		else:
			seen.add(n)