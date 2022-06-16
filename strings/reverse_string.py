def reverse_str(s):
    reversedString = ''
    idx = len(str) - 1  # calculate length of string and save in index

    while idx > 0:
        # save the value of str[index-1] in reverseString
        reversedString += str[idx]
        idx -= 1  # decrement index

    print(reversedString)


def swap(s, i, j):
    strlst = list(s)
    strlst[i], strlst[j] = strlst[j], strlst[j]

    return ''.join(strlst)


def reverse_str_v2(s):
    i = 0
    j = len(s) - 1

    while i < j:
        swap(s, i, j)
        i += 1
        j -= 1


print(reverse_str_v2('hello'))
