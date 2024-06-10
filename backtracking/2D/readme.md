## Matrix - Graph Backtracking

### Questions
1. [200. Number of Islands](https://leetcode.com/problems/number-of-islands/submissions/)
2. [1905. Count Sub Islands](https://leetcode.com/problems/count-sub-islands/)
3. [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
4. [694. Number of Distinct Islands (identical)](https://leetcode.com/problems/number-of-distinct-islands/)
5. [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)
6. [419. Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/)
7. [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
8. [463. Island Perimeter](https://leetcode.com/problems/island-perimeter/)
9. [1254. Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/)
10. [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
11. [79. Word Search](https://leetcode.com/problems/word-search/)
12. [212. Word Search II](https://leetcode.com/problems/word-search-ii/)

### BFS(With BFS Mindset)
1. [733. Flood Fill](https://leetcode.com/problems/flood-fill/)
2. [286. Walls and Gates](https://leetcode.com/problems/walls-and-gates)

## Solution Structure
### 1. Approach
Is `DFS` or `BFS` the best approach to solving the problem?
  
### 2. Neighbours
What are the neighbours of the current cell? In most cases, it's (top, down, left and right) hence can be simplified using delta moves as `[(0, 1), (0, -1), (-1, 0), (1, 0)]`.
```py
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
for dx, dy in directions:
    self.dfs(..., row + dx, col + dy)
```

### 3. Visited Memory
The recursive function needs to keep track of visited nodes to a void going in circles. There are multiple ways to do this;

- Change the visited cell to the value that represents the opposite of traversal state e.g. if you are traversing islands(1), mark the visited cell as (0 -> ocean)

- Change the visited cell to an arbitrary value e.g. `-1` or `#` that will be ignored in the base condition of the recursive call

- Pass a `visited` set that adds all the visited nodes and ignore them in subsequent traversals

`NOTE` - Sometimes, you need to unvisit the visited cell in the current recursive call inorder for subsequent traversals to factor it in.



### 4. Valid Next step
**a. Is cell inbound?**

Is the next neighbour in bound?, i.e.`(0 <= row < n) and (0 <= col < m)`. If not, what is the necessary action to be taken for the backtracking logic?

**b. Is cell visited?**

**c. Is cell a valid state**


### 5. Recursive call return value
1. For DFS, will the `dfs` recursive function return a value, e.g. the `max_area` of the current island or will it operate, e.g. visiting/sinking the island without return anything?


   
