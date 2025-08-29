'''
TIKTOK - LONDON
Two sorted array
input1: [-1, 2, 4, 6] n
input2: [1, 2, 3, 5, 7] m
k = positive integer, e.g. 1, 2 ... n+m

[-1, 1, 2, 2, 3, 4, 5, 6, 7]

kth elements in the merged sorted array
k = 1: return -1
k = 2: return 2
k = 3: reutrn 2
k = 4: return 3
...
k = 8: return 7

1. merge 2 arrays # sorted merged array
2. find kth

input1: [-1, 2] n
input2: [1, 2, 3, 5, 7] m

k = 7
'''


def find_kth_element_v1(arr1, arr2, k):
    n, m = len(arr1), len(arr2)
    i, j = 0, 0

    merged_arr = []

    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[i])
            j += 1

    remaining = arr1[i:] or arr2[j:]
    merged_arr += remaining

    low, high = 0, len(merged_arr)
    while low < high:
        mid = low + (high - low) // 2

        if mid == k - 1:
            return merged_arr[mid]
        elif mid > k - 1:
            high = mid
        else:
            low = mid + 1

    return -1


def find_kth_element_v2(arr1, arr2, k):
    n, m = len(arr1), len(arr2)
    i, j = 0, 0

    count = 1

    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            if count == k:
                return arr1[i]
            i += 1
        else:
            if count == k:
                return arr2[j]
            j += 1

        count += 1

    remaining = arr1[i:] or arr2[j:]
    count, remaining_count = 0, k - count

    while count <= remaining_count:
        if count == remaining_count:
            return remaining[count]

        count += 1

    return -1


print(find_kth_element_v2([-1, 2], [1, 2, 3, 5, 7], 7))
