import random
from typing import Final

NO_OF_TRIALS: Final[int] = 3


class GAME_OF_GUESSING:

    def __init__(self) -> None:
        self.limit = 1

    def __post_init__(self) -> None:
        self.current_guess = self.getGuess()

    def getGuess(self, iteration: int) -> int:
        return random.randrange()

    def play() -> None:
        guess: int = int(input(f'Enter a guess between '))

        # while guess



