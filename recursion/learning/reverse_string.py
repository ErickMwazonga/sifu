# solution 1:
def reverse(str):
    if str == '':
        return ''
    else:
        return reverse(str[1:]) + str[0]

# solution 2:


def reverse(str):
    if len(str) <= 1:
        return str
    else:
        mid = len(str) // 2
        leftPart = str[0:mid]
        rightPart = str[mid:]
        return reverse(rightPart) + reverse(leftPart)

# solution 3:


def rec(str, rev, i=0):
    if i == len(str):
        return
    else:
        rec(str, rev, i+1)
        rev.append(str[i])


def reverse(str):
    rev = []
    rec(str, rev)
    return ''.join(rev)
