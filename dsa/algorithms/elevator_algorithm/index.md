# Elevator Algorithms

## 1. Naive Up/Down (Stops Everywhere)
- Behavior - The elevator moves floor by floor, stopping at every floor, regardless of whether anyone requested it.
- Direction - Moves up until the top, then down until the bottom, continuously reversing.
- Requests - Stops at a floor if requested, but still passes through and records every floor along the way

```py
def naive_elevator(start, requests, floors=10):
    path = []
    direction = 1  # 1 = up, -1 = down
    floor = start
    
    while requests:
        path.append(floor)

        if floor in requests:
            requests.remove(floor)
        
        floor += direction # move

        if floor == floors - 1 or floor == 0:
            direction *= -1

    return path

print("Path:", naive_elevator(0, [2, 8, 3, 7, 1, 9]))
Path: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### Considetaions
- Pros: Very simple to implement.
- Cons: Extremely inefficient; wastes time stopping at floors with no requests.

## 2. Collective Control (Selective Stops)
- Behavior - The elevator moves in one direction but only stops at floors that were requested.
- Direction: Continues moving in the same direction as long as there are requests ahead. Reverses only when no requests remain in that direction.
- Requests - Stops only where needed, skipping unrequested floors.

```py
def collective_elevator(start, requests, floors=10):
    path = []
    direction = 1
    floor = start
    requests = sorted(requests)
    
    while requests:
        path.append(floor)

        if floor in requests:
            requests.remove(floor)

        floor += direction # move

        # reverse if no more requests in direction
        no_above_processing = direction == 1 and (not requests or floor > max(requests))
        no_below_processing = direction == -1 and (not requests or floor < min(requests))

        if no_above_processing or no_below_processing:
            direction *= -1
    
    return path

print("Path:", collective_elevator(0, [2, 8, 3, 7, 1, 9]))
Path: [0, 1, 2, 3, 7, 8, 9]
```

### Considerations
- Pros: More efficient; reduces unnecessary stops.
- Cons: Slightly more complex to implement; needs to track the highest and lowest remaining requests.


## Nearest Car (SSTF-like)

➡️ The elevator always goes to the nearest request (like Shortest Seek Time First in disk scheduling).

def nearest_elevator(start, requests):
    path = [start]
    floor = start
    requests = requests[:]
    
    while requests:
        # pick nearest request
        next_floor = min(requests, key=lambda r: abs(r - floor))
        path.append(next_floor)
        requests.remove(next_floor)
        floor = next_floor
    return path

print("Nearest:", nearest_elevator(0, [2, 8, 3, 7, 1, 9]))


❌ Shortcoming: Far-away requests may starve if closer ones keep appearing.

## SCAN (Classic Elevator Algorithm)

➡️ The elevator moves like a broom: it goes in one direction, serving requests along the way, until it reaches the end (top or bottom), then reverses.

def scan_elevator(start, requests, floors=10, direction=1):
    path = []
    floor = start
    requests = sorted(requests)
    
    while requests:
        path.append(floor)
        if floor in requests:
            requests.remove(floor)
        floor += direction
        if floor == floors or floor < 0:  # reached end
            direction *= -1
            floor += direction  # step back inside bounds
    return path

print("SCAN:", scan_elevator(0, [2, 8, 3, 7, 1, 9]))


❌ Shortcoming: Goes all the way to the end even if no requests exist there.

## LOOK Algorithm

➡️ Improvement over SCAN: elevator goes in one direction but only as far as the last request in that direction, then reverses.

def look_elevator(start, requests, direction=1):
    path = [start]
    floor = start
    requests = sorted(requests)
    
    while requests:
        if direction == 1:
            # serve upward requests
            for r in [f for f in requests if f >= floor]:
                path.append(r)
                requests.remove(r)
                floor = r
            direction = -1
        else:
            # serve downward requests
            for r in [f for f in reversed(requests) if f <= floor]:
                path.append(r)
                requests.remove(r)
                floor = r
            direction = 1
    return path

print("LOOK:", look_elevator(0, [2, 8, 3, 7, 1, 9]))


✅ Advantage: Avoids wasted travel beyond the farthest request.