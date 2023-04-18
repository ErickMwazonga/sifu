# Calculate the factorial of a given number n.

def fib(n: int) -> int:
	if n in [0, 1]:
		return n
	
	return fib(n-1) + fib(n-2)

assert fib(8) == 21