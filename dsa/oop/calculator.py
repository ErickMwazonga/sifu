from typing import TypeAlias, Union

Number: TypeAlias = Union[int, float]

    
class Calculator:

    def addition(self, a: Number, b: Number) -> Number:
        return a + b

    def subtraction(self, a: Number, b: Number) -> Number:
        return a - b

    def multiplication(self, a: Number, b: Number) -> Number:
        return a * b

    def division(self, a: Number, b: Number) -> Number:
        return a / b


class CalculatorUI:

    def __init__(self):
        self.calculator = Calculator()
        self.mapping: dict[int, str] = {
            1: 'ADDITION',
            2: 'SUBTRACTION',
            3: 'MULTIPLICATION',
            4: 'DIVISION'
        }
    
    def calculate(self, choice, *args) -> Number:
        if choice == 1:
            return self.calculator.addition(*args)

        if choice == 2:
            return self.calculator.subtraction(*args)
    
        if choice == 3:
            return self.calculator.multiplication(*args)
        
        if choice == 4:
            return self.calculator.division(*args)
    
    def display_options(self):
        print('OOP SMART CALCULATOR')
        print('*' * 20)

        for key, val in self.mapping.items():
            print(f'{key}: {val}')

    def interact(self):
        while True:
            self.display_options()

            choice = int(input('Enter your choice >>: '))

            if choice not in self.mapping:
                print('You have entered an Invalid option')
            else:
                a = int(input('Enter first number >>: '))
                b = int(input('Enter second number >>: '))

                output = self.calculate(choice, a, b)
                print(f'{self.mapping[choice]} of {a} and {b} is {output}')

            can_proceed_char = input('To continue press y/Y to cancel press any other character >>: ')
            if can_proceed_char not in ['y', 'Y']:
                break
            continue

        print('THANK YOU')


ui = CalculatorUI()
ui.interact()