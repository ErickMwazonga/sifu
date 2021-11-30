'''
main_str = dgfabdghabchdabcgh
substr = abc 
'''


def get_index_of_substr(mainstr, substr):
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
            _count = 0

            for ch in substr:  # O(m)
                if ch != mainstr[i]:
                    break
                i += 1
                _count += 1

            if _count == len_substr:
                results.append(starting_idx)

    return results


assert get_index_of_substr('dgfabdghabchdabcgh', 'abc') == [8, 13]

'''
space - O(n), time - O(n)
'''
