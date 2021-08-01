'''
https://towardsdatascience.com/8-tips-for-object-oriented-programming-in-python-3e98b767ae79
'''

import datetime


class Bank_Account:
    _MIN_BALANCE = 1000

    def __init__(self, owner, account_number, balance=0):
        self._owner = owner
        self._account_number = account_number
        self._created_at = datetime.now().date()

        if balance < self.__MIN_BALANCE:
            raise ValueError("Balance to small!")
        else:
            self._balance = balance

    @property
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def created_at(self):
        return self._created_at

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'

        self.balance = self.balance - amount
        return self.balance

    def __str__(self):
        return f"""
            Bank Account:
            Account Owner: {self.owner}
            Account Number: {self.account_number}
            Creation Date: {str(self.created_at)}
            Current Balance: {self.balance}
        """
