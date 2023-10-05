import random

class ROLL_CALL:

    def __init__(self, users=[]) -> None:
        self.users: list[str] = users
        self.current_roll_call: list[str] = []

    def get_users(self) -> list[str]:
        return self.users

    def add_user(self, name: str) -> str | None:
        if name in self.users:
            return "User already exists"

        self.users.append(name)
        print(f"{name} added to the roll call!")

    def add_users(self, users: list[str]) -> None:
        for user in users:
            if user not in self.users:
                self.users.append(user)

        print("Operation to add users completed!!")

    def generate_roll_call(self) -> list[str]:
        if self.current_roll_call:
            return self.current_roll_call

        curr_roll_call = [*self.users]
        random.shuffle(curr_roll_call)
        self.current_roll_call = curr_roll_call

        print(self.users)
        return curr_roll_call


users = ['Erick', 'Kishore', 'Jazib', 'Lucio', 'Andrea', 'Claudette', 'Charbel', 'Ranjithkumar']

roll_call = ROLL_CALL()
roll_call.add_users(users)
roll_call.generate_roll_call()
