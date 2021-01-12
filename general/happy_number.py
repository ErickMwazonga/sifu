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
    '''https://leetcode.com/problems/happy-number/discuss/566036/Math-Approach-with-Python-3-Solution'''

    seen = set()
    
    while True:
        if n in seen:
            return False
        elif n == 1:
            return True
        else:
            seen.add(n)
            n = sum([int(x) ** 2 for x in str(n)])

# FLOYD'S APPROACH
'''
https://leetcode.com/problems/happy-number/discuss/843860/Python-3-greater-tortoise-hare-technique
'''
def isHappy(self, n: int) -> bool:
	#20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
	slow = self.squared(n)
	fast = self.squared(self.squared(n))

	while slow != fast and fast != 1:
		slow = self.squared(slow)
		fast = self.squared(self.squared(fast))

	return fast == 1

def squared(self, n):
	result = 0

	while n > 0:
		last = n % 10
		result += last * last
		n = n // 10

	return result