'''
Given a string and substring, return the indexes of first char of the substring in the main string
Input
    mainstr = dgfabdghabchdabcgh
    substr = abc 
Output - [8, 11]
'''


def get_index_of_substr(mainstr, substr):
    '''space - O(n), time - O(n)'''

    len_mainstr, len_substr = len(mainstr), len(substr)
    results = []

    if len_substr > len_mainstr:
        return -1

    if len_substr == len_mainstr and mainstr != substr:
        return -1

    i, j = 0, 0

    while i < len_mainstr:  # O(n)
        if mainstr[i] != substr[j]:
            i += 1
        else:
            starting_idx = i
            is_substring = True

            for ch in substr:  # O(m)
                if ch != mainstr[i]:
                    is_substring = False
                    break

                i += 1

            if is_substring:
                results.append(starting_idx)

    return results


assert get_index_of_substr('dgfabdghabchdabcgh', 'abc') == [8, 13]
