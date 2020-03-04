def swap(string, i, j):
    strlst = list(string)
    temp = strlst[i]
    strlst[i] = strlst[j];
    strlst[j] = temp;
    return "".join(strlst)

def reverse(string):
    i = 0
    j = len(string) - 1
    while (i < j):
        swap(string, i, j)
        i += 1
        j -= 1

print(reverse('hello'))
