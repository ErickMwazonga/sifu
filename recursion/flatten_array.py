'''
[1, 2, 3] -> [1, 2, 3]
[1, [2, 3], [1], [], 5, [6, [7, 9]]] -> [1, 2, 3, 1, 5, 6, 7, 9]
'''

def flatten(arr, res = []):
    for x in arr:
        if not isinstance(x, list):
            res.append(x)
            continue
        flatten(x, res)
        
    return res


def flatten_v1(arr):
    if not arr:
        return []
    
    if isinstance(arr[0], list):
        return flatten(arr[0]) + flatten(arr[1:])
    
    return [arr[0]] + flatten(arr[1:])

def flatten_v2(arr, start=0):
    if start == len(arr):
        return []
    
    if isinstance(arr[start], list):
        return flatten(arr[start]) + flatten(arr, start+1)
    
    return [arr[start]] + flatten(arr, start+1)

def flatten_v3(arr):
    result, stack = [], [arr]
    
    while stack:
        item = stack.pop()
        
        if isinstance(item, list):
            stack.extend(reversed(item))
        else:
            result.append(item)
            
    return result

def flatten_v4(arr):
    for item in arr:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
            
_input1 = [1, [2, 3], [1], [], 5, [6, [7, 9]]]
_input2 = [1, [2, 3], [4, 5, [6, [7, 8], 9], 10, [11, 12]]]

print(flatten(_input1))