'''
https://www.geeksforgeeks.org/reduce-a-number-to-1-by-performing-given-operations/
Reduce a number to 1 by performing given operations
Given a number N. The task is to reduce the given number N to 1 in the minimum number of steps.
You can perform any one of the below operations in each step.

Operation 1: If the number is even then you can divide the number by 2.
Operation 2: If the number is odd then you are allowed to perform either (n+1) or (n-1).

Input : n = 15
Output : 5
 15 is odd 15+1=16    
 16 is even 16/2=8     
 8  is even 8/2=4 
 4  is even 4/2=2     
 2  is even 2/2=1     

Input : n = 7
Output : 4
    7->6  6->3  3->2  2->1  
'''


def count_ways(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + count_ways(n / 2)
    else:
        return 1 + min(count_ways(n - 1), count_ways(n + 1))


print(count_ways(15))
