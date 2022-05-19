'''
384. Shuffle an Array
https://leetcode.com/problems/shuffle-an-array/
Resource: Inspired by - https://www.youtube.com/watch?v=4zx5bM2OcvA

Given an integer array nums, design an algorithm to randomly shuffle the array.
Implement the Solution class:
Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
'''

import random


def shuffle(A) -> list[int]:
    '''Time: O(n**2), Space: O(n)'''

    shuffled = []

    while len(A):
        rand_idx = random.randrange(0, len(A))
        shuffled.append(A[rand_idx])
        A.pop(rand_idx)

    A = shuffled
    return A


def shuffle_v2(A) -> list[int]:
    '''
    Returns a random shuffling of the array.
    Inspired by - https://www.youtube.com/watch?v=4zx5bM2OcvA
    '''

    last_index = len(A) - 1

    while last_index > 0:
        rand_index = random.randint(0, last_index)
        A[last_index], A[rand_index] = A[rand_index], A[last_index]
        last_index -= 1

    return A
