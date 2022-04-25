def reverse(str):
    if str == '':
        return ''
    else:
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


def reverse(str):
    rev = []
    rec(str, rev)
    return ''.join(rev)
