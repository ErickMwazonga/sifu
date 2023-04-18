# Check if a given string is a palindrome.

def is_palindrome(text: str) -> bool:
	return traverse(text, 0, len(text) - 1)

def traverse(text: str, i: int, j: int) -> bool:
	if i > j:
		return True
	
	if text[i] != text[j]:
		return False
	
	return traverse(text, i + 1, j - 1)

assert is_palindrome('mama') == False
assert is_palindrome('akka') == True
		
	