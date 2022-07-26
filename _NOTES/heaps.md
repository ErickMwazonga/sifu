# Heaps
## Time Complexites
`heapq.heapify()` -> `O(n)` </br>
> Transform list x into a heap, in-place, in linear time. </br>

`heapq.heappush()` -> `O(logn)` </br>
`heapq.heappop()` ->  `O(logn)` </br> </br>

## Min Heap
```py
>>> import heapq
>>> heapq.heapify(lst)
```

## Max Heap
Max heap is not supported by default by heapq module in python.<br/>
However, there are some workaround to simulate/implement it.

1. `heapq._heapify_max(lst)`

```py
>>> lst: list[int] = [5, 1, 3, 7, 2]

>>> heapq._heapify_max(lst)
>>> pop_max = heapq._heappop_max(lst)
```
2. **Using Negatives**

```py
>>> array: list[int] = [1, 4, 6, 2, 5, 3, 9, 8, 7]
>>> maxHeap = []
>>> for num in array:
        heapq.heappush(maxHeap, -num)

>>> print('maxHeap:', maxHeap)
# maxHeap: [-9, -8, -6, -7, -2, -3, -4, -1, -5]
```

## Multiple Items Heap
Heap elements can be tuples. <br/>
This is useful for assigning comparison values (such as task priorities) alongside the main record being tracked
```py
>>> lst = [
    (5, 'write code'),
    (7, 'release product'), 
    (1, 'write spec'),
    (3, 'create tests')
]
>>> heap = []
>>> for num in array:
        heappush(heap, num)

>>> heappop(heap)
# (1, 'write spec')
```