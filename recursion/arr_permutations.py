def getPermutations(arr):
    if len(arr) < 2:
        return [arr]
    else:
        permutations = []

        for i in range(len(arr)):
            if arr[i] not in arr[:i]:
                remaining = arr.copy()
                remaining.pop(i)
                remainingPermutations = getPermutations(remaining)
                removedElement = [arr[i]]
                
                for permutation in remainingPermutations:
                    permutations.append(removedElement + permutation)
                    
        return permutations