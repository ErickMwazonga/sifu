from abc import ABC
from .constants import AccountStatus


class Account(ABC):
    def __init__(self, id, password, person, status=AccountStatus.NONE):
        self.__id = id
        self.__password = password
        self.__status = AccountStatus.NONE
        self.__person = person

    def reset_password(self):
        pass


class Member(Account):
    def __init__(self, date_joined):
        date_joined = date_joined

    def search_member(self):
        ...


class AdditionalDriver:
    def __init__(self, id, person):
        self.__driver_id = id
        self.__person = person
