from utilities import card_utilities
from utilities import strategies
from structures.card import Card
import random

class CardsNotSeen(object):

    def __init__(self):
        self.__cards_remaining = card_utilities.create_deck()

    def cards_remaining(self):
        return self.__cards_remaining

    def num_cards_remaining(self):
        return len(self.cards_remaining())

    def done(self):
        if self.__num_cards_remaining == 0:
            return True
        else:
            return False

    def print_remaining_cards(self):
        for card in self.__cards_remaining:
            print(str(card))

    def remove_card(self,card):
        self.__cards_remaining.remove(card)

    def cards_playable(self,card):
        if isinstance(card,str):
            return self.cards_remaining()
        else:
            return [elem for elem in self.cards_remaining() if (elem.suit != card.suit and elem.value != card.value)]

    def random_card(self,card):
        if isinstance(card, str):
            return random.choice(self.cards_remaining())
        else:
            return random.choice(self.cards_playable(card))

    def play_suits_strategy(self,card):
        if isinstance(card, str):
            return random.choice(self.cards_remaining())
        else:
            return strategies.suit_first(self.cards_playable(card))

    def play_val_strategy(self, card):
        if isinstance(card, str):
            return random.choice(self.cards_remaining())
        else:
            return strategies.num_first(self.cards_playable(card))