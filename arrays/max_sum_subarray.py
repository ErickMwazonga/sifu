# Returns true if the there is a subarray 
# of arr[] with sum equal to 'sum'  
# otherwise returns false. Also, prints the result 

def subArraySum(arr, sum):
    """Time Complexity : O(n^2) in worst case."""
    n = len(arr)

    for i in range(n): 
        curr_sum = arr[i]

        j = i + 1
        while j <= n:
            if curr_sum == sum: 
                print ("Sum found between") 
                print(f"indexes {i} and {j-1}") 
                return 1
            
            if curr_sum > sum or j == n: 
                break
            
            curr_sum += arr[j] 
            j += 1
        
    print ("No subarray found") 
    return 0

arr = [15, 2, 4, 8, 9, 5, 10, 23] 
_sum = 23

arr1 = [3, 4, -7, 1, 3, 3, 1, -4]
_sum1 = 7

arr2 = [-10, 0, 2, -2, -20, 10]
_sum2 = 20
  
subArraySum(arr2, _sum2) 