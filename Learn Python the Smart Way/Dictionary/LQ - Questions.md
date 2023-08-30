## Questions

### Q1 - Given a list, find the mos frequent number

```py
nums = [1, 2, 3, 4, 2, 5, 2, 6] -> 2
nums = [1, 2, 3, 4, 9, 5, 6, 9] -> 9

def mos_frequent(nums: list[nums]) -> int:
    freqs = {}
    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1

    most_frequent = -1
    for num, freq in freqs:
        if freq > most_frequent:
            most_frequent = freq

    return most_frequent
```
