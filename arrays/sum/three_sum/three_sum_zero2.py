def threeSum(nums):
    lis =[]
    nums.sort()

    for i in range(len(nums)-2):
        low = i + 1
        high = len(nums) - 1
        
        while (low < high):
            s = nums[i] + nums[low] + nums[high]
            
            if s == 0:
                lis.append((nums[i], nums[low], nums[high]))
                low = low + 1
                high = high - 1
            
            if s < 0:
                low = low + 1

            if s > 0:
                high = high - 1
                
    res = list(set(lis))     
    res = [list(x) for x in res]
    return res

a = [-1, 0, 1, 2, -1, -4]

print(threeSum(a))