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

### Q2 - Given 2 strings, check if they are anagrams

```py
'''
Examples

bored, robed -> True
cat, act -> True
inch, chin -> True
school, chola -> False
'''

def anagram1(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)


def anagram2(a: str, b: str) -> bool:
    a_freq, b_freq = {}, {}

    for ch in a:
        a_freq[ch] = a_freq.get(ch, 0) + 1

    for ch in b:
        b_freq[ch] = b_freq.get(ch, 0) + 1

    for key in a_freq:
        # if a_freq[key] != b_freq[key]: # but the key might not be there
        if a_freq[key] != b_freq.get(ch, 0):
            return False

    return True
```
