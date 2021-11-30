'''
https://www.codespeedy.com/kmp-string-matching-algorithm-in-python/
'''


def KMP_String(pattern, text):
    a = len(text)
    b = len(pattern)

    prefix_arr = get_prefix_arr(pattern)

    initial_point = []

    i, j = 0, 0

    while i != a:

        if text[i] == pattern[j]:
            i += 1
            j += 1

        else:
            j = prefix_arr[j-1]

        if j == b:
            initial_point.append(i-j)
            j = prefix_arr[j-1]
        elif n == 0:
            j += 1

    return initial_point


def get_prefix_arr(pattern):
    b = len(pattern)

    prefix_arr = [0] * b
    n = 0
    m = 1

    while m != b:
        if pattern[m] == pattern[n]:
            n += 1
            prefix_arr[m] = n
            m += 1
        elif n != 0:
            n = prefix_arr[n-1]
        else:
            prefix_arr[m] = 0
            m += 1

    return prefix_arr


string = 'ABABDABACDABABCABABCABAB'
pat = 'ABABCABAB'

initial_index = KMP_String(pat, string)

for i in initial_index:
    print('Pattern is found in the string at index number', i)
