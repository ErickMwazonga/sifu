'''
Police Officers Catch the Thieves!

You are given an array of size n in which each element contains either a 'P' for policeman or a 'T' for thief and an integer value k. 
Maximize the number of thieves that can be caught by the police.

The constraints are :
A police can catch at most one thief.
A police cannot catch a thief who is more than K units away from him.

There are two ways to catch a thief.
CASE 1: The thief to be caugth lies to the left of the police.
CASE 2: The thief to be caugth lies to the right of the police.

Examples
1. [T, P, P, P, T, T, T], K = 2 -> 3
    Explanation
    P at index 1 will catch T at index 0.
    P at index 2 will catch T at index 4.
    P at index 3 will catch T at index 5.

2. [T, T, P, P, T, P, T, P], k = 2 -> 4
3. [P, T, T, P, T], k = 1 -> 2.
    Here maximum 2 thieves can be caught, first
    policeman catches first thief and second police-
    man can catch either second or third thief.
4. [T, T, P, P, T, P], k = 2 -> 3
5. [P, T, P, T, T, P], k = 3 -> 3
'''
