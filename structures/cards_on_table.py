from utilities import card_utilities
import random

class CardsOnTable(object):

    def __init__(self, num_cards = 10):
        self.__deck = card_utilities.create_deck()
        self.__unseen_cards_on_table = random.sample(self.__deck, num_cards)
        self.__num_cards = num_cards
        self.__cards_seen = []

    def cards_on_table(self):
        return self.__unseen_cards_on_table

    def num_cards_on_table(self):
        return len(self.cards_on_table())

    def remaining_deck(self):
        non_table =  [x for x in self.__deck if x not in self.__unseen_cards_on_table]
        for x in self.__cards_seen:
            non_table.remove(x)
        return non_table

    def leading_card(self):
        return self.__unseen_cards_on_table[0]

    def check_suggestion(self, card):
        leading_card = self.__unseen_cards_on_table[0]
        if card == leading_card:
            return "correct"
        elif card.suit == leading_card.suit:
            return "suit"
        elif card.value == leading_card.value:
            return "number"
        else:
            return "incorrect"

    def pop_card(self,num):
        self.__cards_seen = self.__cards_seen + [self.__unseen_cards_on_table[0]]
        self.__unseen_cards_on_table = self.__unseen_cards_on_table[num:]


    def add_card(self,num):
        for i in range(1,num + 1):
            if self.num_cards_on_table() < self.__num_cards:
                to_append = random.choice(self.remaining_deck())
                self.__unseen_cards_on_table = self.cards_on_table() + [to_append]