from enum import Enum
from abc import ABC, abstractmethod
from typing import Optional
from datetime import datetime, timedelta

class VehicleType(Enum):
    CAR = "Car"
    BIKE = "Bike"
    TRUCK = "Truck"


class SpotType(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

# Vihicle representation
class Vehicle(ABC):

    def __init__(self, license_plate: str):
        self.license_plate: str = license_plate
        self.parked_spot: Optional[Spot] = None

    @property
    @abstractmethod
    def vehicle_type(self) -> VehicleType:
        pass


class Car(Vehicle):
    @property
    def vehicle_type(self) -> VehicleType:
        return VehicleType.CAR


class Bike(Vehicle):
    @property
    def vehicle_type(self) -> VehicleType:
        return VehicleType.BIKE


class Truck(Vehicle):
    @property
    def vehicle_type(self) -> VehicleType:
        return VehicleType.TRUCK


# Parking Spot representation
class Spot:

    def __init__(self, spot_id: str, size: SpotType):
        self.spot_id: str = spot_id
        self.type: SpotType = type
        self.current_vehicle: Optional[Vehicle] = None
        self.parked_at: Optional[datetime] = None

    def __str__(self) -> str:
        return f"Spot({self.spot_id}, {self.size.name})"

    @property
    def is_available(self) -> bool:
        return not self.current_vehicle

    def park(self, vehicle: Vehicle) -> bool:
        if not self.can_fit(vehicle):
            raise ValueError(f"{vehicle.vehicle_type.name} cannot fit in spot {self}")
        
        if not self.is_available:
            return ValueError(f"Spot {self} is already occupied")
        
        self.current_vehicle = vehicle
        self.parked_at = datetime.now()
        vehicle.parked_spot = self

    def leave(self) -> None:
        self.current_vehicle = None
        self.parked_at = None
        self.current_vehicle.parked_spot = None

    def can_fit_vehicle(self, vehicle: Vehicle) -> bool:
        vehicle_spot_mapping = {
            VehicleType.BIKE: [SpotType.SMALL, SpotType.MEDIUM, SpotType.LARGE],
            VehicleType.CAR: [SpotType.MEDIUM, SpotType.LARGE],
            VehicleType.TRUCK: [SpotType.LARGE]
        }
        return self.size in vehicle_spot_mapping.get(vehicle.vehicle_type, [])
    

# Parking Level representation
class Level:

    def __init__(self, level_id: str, spots: list[Spot]):
        self.level_id: str = level_id
        self.spots: list[Spot] = spots

    def find_available_spot(self, vehicle: Vehicle) -> Optional[Spot]:
        for spot in self.spots:
            if spot.is_available and spot.can_fit_vehicle(vehicle):
                return spot
        return None
    
    @property
    def available_spots(self) -> int:
        return sum(1 for spot in self.spots if spot.is_available)
    
    @property
    def is_full(self) -> bool:
        return self.available_spots == 0
    

# Parking Lot representation
class ParkingLot:

    def __init__(self, levels: list[Level]):
        self.levels: list[Level] = levels

    def park(self, vehicle: Vehicle) -> bool:
        # If vehicle is already parked, prevent double parking
        if vehicle.parked_spot:
            print(f"Vehicle {vehicle.license_plate} is already parked at {vehicle.parked_spot}")
            return False
        
        for level in self.levels:
            spot = level.find_available_spot(vehicle)
            if spot:
                spot.park(vehicle)
                print(f"Parked {vehicle.vehicle_type.name} at {spot} on level {level.level_id}")
                return True
            
        print(f"No available spot for {vehicle.vehicle_type.name}")
        return False

    def remove_vehicle(self, vehicle: Vehicle) -> bool:
        if not vehicle.parked_spot:
            print(f"Vehicle {vehicle.license_plate} not found in parking lot")
            return False
    
        spot = vehicle.parked_spot
        level_id = next((lvl.level_id for lvl in self.levels if spot in lvl.spots), "Unknown")
        spot.remove_vehicle()
        print(f"Removed vehicle {vehicle.license_plate} from {spot} on level {level_id}")
        return True

    def find_vehicle_spot(self, vehicle: Vehicle) -> Optional[Spot]:
        return vehicle.parked_spot