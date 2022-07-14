def reverse_str(s: str) -> str:
    reversedString = ''
    idx = len(s) - 1  # calculate length of string and save in index

    while idx > 0:
        # save the value of str[index-1] in reverseString
        reversedString += s[idx]
        idx -= 1  # decrement index

    return reversedString


def swap(s: str, i: int, j: int) -> str:
    strlst = list(s)
    strlst[i], strlst[j] = strlst[j], strlst[i]

    return ''.join(strlst)


def reverse_str_v2(s: str) -> str:
    i, j = 0, len(s) - 1

    while i <= j:
        s = swap(s, i, j)
        i, j = i + 1, j - 1

    return s


assert reverse_str_v2('hello') == 'olleh'
