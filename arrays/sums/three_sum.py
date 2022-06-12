'''
Find a triplet that sum to a given value

Given an array and a value, find if there is a triplet in array
whose sum is equal to the given value.
If there is such a triplet present in array, then print the triplet
and return true. Else return false.

For example,
if the given array is [12, 3, 4, 1, 6, 9] and given sum is 24,
then there is a triplet [12, 3 and 9] present in array whose sum is 24.
'''


def three_sum(nums, target):
    '''Time: 0(n^2)'''

    nums.sort()
    n, res = len(nums), set()

    for i in range(n):
        target = target - nums[i]
        j, k = i + 1, n - 1

        while j < k:
            _sum = nums[j] + nums[k]

            if _sum == target:
                res.add([nums[i], nums[j], nums[k]])
                return True
            elif _sum > target:
                k -= 1
            else:
                j += 1

    return False


assert three_sum([12, 3, 4, 1, 6, 9], 24) == True
assert three_sum([12, 3, 4, 1, 6, 9], 28) == False
