'''
384. Shuffle an Array
https://leetcode.com/problems/shuffle-an-array/

Given an integer array nums, design an algorithm to randomly shuffle the array.
Implement the Solution class:
Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
'''


class Solution:

    def __init__(self, A: list[int]):
        self.A = A
        self.original_nums = A[:]

    def reset(self) -> list[int]:
        '''Resets the array to its original configuration and return it.'''
        return self.original_nums

    def shuffle(self) -> list[int]:
        '''
        Returns a random shuffling of the array.
        Inspired by - https://www.youtube.com/watch?v=4zx5bM2OcvA
        '''
        import random

        last_index = len(self.A) - 1
        while last_index > 0:
            rand_index = random.randint(0, last_index)
            self.A[last_index], self.A[rand_index] = self.A[rand_index], self.A[last_index]
            last_index -= 1

        return self.A
