from ast import Add
from .constants import Address


class CarRentalLocation:
    def __init__(self, name, address) -> None:
        self.__name: str = name
        self.__location: Address = address

    def get_location(self) -> Address:
        return self.__location


class CarRentalSystem:
    def __init__(self, name):
        self.__name = name
        self.__locations = []

    def add_new_location(self, location):
        None
