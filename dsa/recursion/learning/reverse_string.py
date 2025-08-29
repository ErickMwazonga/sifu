def reverse(str):
	if str == '':
		return ''

	return reverse(str[1:]) + str[0]


def reverse_v2(str):
    if len(str) <= 1:
        return str
    else:
        mid = len(str) // 2
        leftPart = str[0:mid]
        rightPart = str[mid:]
        return reverse(rightPart) + reverse(leftPart)


def reverse_v3(str, rev, i=0):
    if i == len(str):
        return
    else:
        reverse_v3(str, rev, i+1)
        rev.append(str[i])


def reverse_v4(_str):
    rev = []
    reverse(_str, rev)
    return ''.join(rev)


def reverse_string(text: str) -> str:
	if len(text) in [0, 1]:
		return text

	return reverse_string(text[1:]) + text[0]

def reverse_string_v2(text: str) -> str:
	def traverse(text: str, i: int) -> str:
		if i == len(text) - 1:
			return text[i]

		return traverse(text, i + 1) + text[i]

	return traverse(text, 0)

assert reverse_string('hello') == reverse_string_v2('hello') == 'olleh'
