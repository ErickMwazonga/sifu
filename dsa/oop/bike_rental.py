'''
A Bike Rental System
CREDIT: https://medium.com/@gurupratap.matharu/object-oriented-programming-project-in-python-for-your-github-portfolio-d34feaf1332c
A full fledged bike rental system implemented in Python using object oriented programming.

Customers can
    - See available bikes on the shop
    - Rent bikes on hourly basis $5 per hour.
    - Rent bikes on daily basis $20 per day.
    - Rent bikes on weekly basis $60 per week.
    - Family Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price

The bike rental shop can
    - issue a bill when customer decides to return the bike.
    - display available inventory
    - take requests on hourly, daily and weekly basis by cross verifying stock

For simplicity we assume that
    - Any customer requests rentals of only one type i.e hourly, monthly or weekly
    - Is free to choose the number of bikes he/she wants
    - Requested bikes should be less than available stock.
'''

import datetime


class BikeRental:

    def __init__(self, stock=0):
        self.stock = stock

    def displaystock(self):
        '''Displays the bikes currently available for rent in the shop.'''

        print(f'We have currently {self.stock} bikes available to rent.')
        return self.stock

    def rentBikeOnHourlyBasis(self, n):
        '''Rents a bike on hourly basis to a customer.'''

        if n <= 0:
            print('Number of bikes should be positive!')
            return None
        elif n > self.stock:
            msg = f'Sorry! We have currently {self.stock} bikes available to rent.'
            print(msg)
            return None
        else:
            now = datetime.datetime.now()
            msg = f'You have rented a {n} bike(s) on hourly basis today at {now.hour} hours.'
            print(msg)
            print('You will be charged $5 for each hour per bike.')
            print('We hope that you enjoy our service.')

            self.stock -= n
            return now

    def rentBikeOnWeeklyBasis(self, n):
        '''Rents a bike on weekly basis to a customer.'''

        if n <= 0:
            print('Number of bikes should be positive!')
            return None
        elif n > self.stock:
            msg = f'Sorry! We have currently {self.stock} bikes available to rent.'
            print(msg)
            return None

        else:
            now = datetime.datetime.now()
            msg = f'You have rented a {n} bike(s) on weekly basis today at {now.hour} hours.'
            print(msg)
            print('You will be charged $60 for each week per bike.')
            print('We hope that you enjoy our service.')

            self.stock -= n
            return now

    def returnBike(self, request):
        '''
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        '''

        # extract the tuple and initiate bill
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0
        # issue a bill only if all three parameters are not null!
        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes

            # daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes

            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes

            # family discount calculation
            if (3 <= numOfBikes <= 5):
                print('You are eligible for Family rental promotion of 30% discount')
                bill = bill * 0.7

            print('Thanks for returning your bike. Hope you enjoyed our service!')
            print('That would be ${}'.format(bill))
            return bill

        else:
            print('Are you sure you rented a bike with us?')
            return None


class Customer:
    def __init__(self):
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):
        '''Takes a request from the customer for the number of bikes.'''

        bikes = input('How many bikes would you like to rent?')

        try:
            bikes = int(bikes)
        except ValueError:
            print('That\'s not a positive integer!')
            return -1
        if bikes < 1:
            print('Invalid input. Number of bikes should be greater than zero!')
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def returnBike(self):
        '''Allows customers to return their bikes to the rental shop.'''

        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0, 0, 0
