from typing import Enum
from operator import ge, le

class Direction(Enum):
    UP = 1
    DOWN = -1

class Elevator:
    def __init__(self, floors: int):
        self.floors = floors
        self.current_floor = 0
        self.direction = Direction.UP
        self.requests = set()
        self.optimal_floor = self.total_floors // 2

    def add_request(self, floor: int):
        '''Add a floor request (e.g., button press inside or call from outside).'''

        if 0 > floor > self.floors:
            raise ValueError("Floor out of range")
        self.requests.add(floor)

    def _filter_floors(self, direction: Direction):
        '''Utility method to filter floors based on a condition relative to current floor.'''

        comparison = ge if direction == Direction.UP else le
        return [f for f in self.requests if comparison(f, self.current_floor)]

    def next_floor(self):
        '''Determine the next floor to go to based on current state and requests.'''

        if not self.requests:
            # If idle and not at optimal floor, move to optimal floor
            if self.current_floor != self.optimal_floor:
                return self.optimal_floor
            return None
        
        floors_in_direction = self._filter_floors(self.direction)
        if floors_in_direction:
            return min(floors_in_direction) if self.direction == Direction.UP else max(floors_in_direction)
        else:
            # No requests in current direction, reverse direction
            self.direction = Direction.DOWN if self.direction == Direction.UP else Direction.UP
            floors_in_opposite = self._filter_floors(self.direction)

            if floors_in_opposite:
                return min(floors_in_opposite) if self.direction == Direction.UP else max(floors_in_opposite)
            else:
                # No requests at all, stay idle
                if self.current_floor != self.optimal_floor:
                    return self.optimal_floor
        
        return self.optimal_floor

    def move(self):
        """Move the elevator to the next floor and process the request."""

        next_stop = self.next_floor()
        if next_stop is None:
            print("Elevator idle at floor", self.current_floor)
            return

        print(f"Elevator moving from floor {self.current_floor} to {next_stop}")
        self.current_floor = next_stop
        self.requests.discard(next_stop)

        # Update direction based on remaining requests
        if not self.requests:
            self.direction = Direction.UP  # Default to up when idle
            if self.current_floor != self.optimal_floor:
                print(f"No requests. Moving to optimal floor {self.current_floor}.")
                self.add_request(self.optimal_floor)  # Move to optimal floor
        else:
            if self.current_floor >= max(self.requests):
                self.direction = Direction.DOWN # At highest request, go down
            elif self.current_floor <= min(self.requests):
                self.direction = Direction.UP # At lowest request, go up
        