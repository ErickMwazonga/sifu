"""
Count of index pairs with equal elements in an array
Given an array of n elements.
The task is to count the total number of indices (i, j) such that arr[i] = arr[j] and i != j

Examples :
Input : arr[] = {1, 1, 2}
Output : 1
As arr[0] = arr[1], the pair of indices is (0, 1)

Input : arr[] = {1, 1, 1}
Output : 3
As arr[0] = arr[1], the pair of indices is (0, 1), 
(0, 2) and (1, 2)

Input : arr[] = {1, 2, 3}
Output : 0
"""


def countPairs2(arr):
    """Time Complexity : O(n)"""
    n = len(arr)
    mp = {}

    # Finding frequency of each number.
    for i in range(n):
        elem = arr[i]
        if elem in mp.keys():
            mp[elem] = mp.get(elem, 0) + 1

    # Calculating pairs of each value.
    ans = 0
    for it in mp:
        count = mp[it]
        ans += (count * (count - 1)) // 2
    return ans


def countPairs3(arr):
    def no_of_repeats(n):
        if n < 2:
            return 0
        return n-1 + no_of_repeats(n-1)

    freqs = [arr.count(i) for i in list(set(arr))]
    res = sum([no_of_repeats(i) for i in freqs])
    return res


def countPairs4(arr):
    freqs = [arr.count(i) for i in list(set(arr))]

    def no_of_repeats(n):
        return (n * (n - 1)) // 2

    res = sum([no_of_repeats(i) for i in freqs])
    return res


arr = [1, 1, 2] 
arr1 = [1, 1, 1, 3, 3, 4, 1]
# print(countPairs(arr))
print(countPairs2(arr1))
print(countPairs3(arr1))
