import random
from datetime import datetime
from enum import Enum, unique
from typing import Union


@unique
class SUIT(Enum):
    # HEART, SPADE, CLUB, DIAMOND = 1, 2, 3, 4
    HEART, SPADE, CLUB, DIAMOND = range(1, 5)


class Card:
    def __init__(self, suit: str, val: int):
        self.__suit = suit
        self.__value = val

    def __str__(self) -> str:
        return self.show

    @property
    def suit(self) -> str:
        return self._suit

    @suit.setter
    def suit(self, suit) -> None:
        if suit in SUIT.__members__.keys():
            self.__suit = suit
        else:
            print('Thats not a suit!')

    def get_value(self) -> int:
        return self.__value

    def show(self) -> str:
        mapping: dict[int, str] = {
            1: 'Ace',
            11: 'Jack',
            12: 'Queen',
            13: 'King'
        }
        other_cards: dict[int, int] = {x: x for x in range(2, 11)}
        all_cards = mapping | other_cards
        val = all_cards[self.__value]

        return f'{val} of {self.suit}'


class Deck:
    def __init__(self):
        self.__cards: list[Card] = []
        self.__creation_date: datetime = datetime.date.today()

        self.build()

    def build(self) -> None:
        for value in range(1, 14):
            for suit in SUIT:
                new_card = Card(suit, value)
                self.__cards.add(new_card)

    def show(self) -> None:
        for card in self.__cards:
            print(card.show())

    def get_cards(self) -> list[Card]:
        self.__cards

    def shuffle(self) -> None:
        random.shuffle(self.__cards)

    def draw_card(self) -> Union[Card, None]:
        return self.__cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def sayHello(self):
        print('Hi! My name is {self.name}')

    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False
        return True

    def showHand(self):
        print(f"self.name's hand: {self.hand}")

    def discard(self):
        return self.hand.pop()
