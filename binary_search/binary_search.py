# Linear Search
def linear_search(data, target):	
	for i in range(len(data)):
		if data[i] == target:
			return True
	return False

# ITERATIVELY
def binarySearch(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high: 
        mid = low + (high - low) // 2 # To prevent overflow
          
        if x == arr[mid]: 
            return mid 
        elif x > arr[mid]: 
            low = mid + 1
        else: 
            high = mid - 1
    return -1 # NOT FOUND

# RECURSIVE
def binarySearch2(arr, low, high, x):
    if low <= high:
        mid = low + (high - low) // 2

        if x == arr[mid]: 
            return mid
        elif x > arr[mid]: 
            return binarySearch2(arr, mid+1, high, x)
        else: 
            return binarySearch2(arr, low, mid-1, x) 
    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10
low, high = 0, len(arr) - 1
  
# print(binarySearch(arr, x))
print(binarySearch2(arr, low, high, x))