# Mutability

## Mutable Objects - List
```py
def recursive_function(res: list[int]) -> list[int]:
    res.extend([3, 4])
    return res

>>> res: list[int] = [1, 2]
>>> recursive_function(res) # [1, 2, 3, 4]
>>> res # [1, 2, 3, 4]

# Application Example
class Solution:
    def addNum(self, num: int) -> list[int]:
        res: list[int] = [1, 2]
        self.dfs(num, res)
        return res
    
    def dfs(self, num: int, res: list) -> None:
        res.append(num)
        return

>>> soln = Solution()
>>> soln.addNum(99) # [1, 2, 99]
``` 
## Immutable Objects - Boolean
```py
def recursive_function(found: bool) -> bool:
    found: bool = True
    return found

>>> found: bool = False
>>> recursive_function(found) # True
>>> found # False

# Application Example
class Solution:
    def addPath(self) -> bool:
        hasPath: bool = False
        self.dfs(hasPath)
        return hasPath
    
    def dfs(self, hasPath: bool) -> None:
        hasPath = True
        return

>>> soln = Solution()
>>> soln.addPath() # False instead of True(Modified in the dfs funtion)

# Solution to passing Immutable objects to a funciton
class Solution:
    def addPath(self) -> bool:
        hasPath: list[bool] = [False]
        self.dfs(hasPath)
        return hasPath[0]
    
    def dfs(self, hasPath: list[bool]) -> None:
        hasPath[0] = True
        return

>>> soln = Solution()
>>> soln.addPath() # True -> Since list is mutable
```