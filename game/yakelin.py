from structures import cards_not_seen
from structures import cards_on_table

import random

class Yakelin(object):
    def __init__(self,numcards = 10):
        self.__hand = cards_not_seen.CardsNotSeen()
        self.__table = cards_on_table.CardsOnTable(numcards)

    def print_remaining(self):
        self.__hand.print_remaining_cards()

    def play_card(self, prev_card, to_play):
        #You lose if there are no possible cards to play
        if len(self.__hand.cards_playable(prev_card)) == 0:
            return "LOSE"
        #Choose a card to play depending on the strategy you want to play
        if to_play == "random":
            to_play = self.__hand.random_card(prev_card)
        elif to_play == "suits_strat":
            to_play = self.__hand.play_suits_strategy(prev_card)
        elif to_play == "val_strat":
            to_play = self.__hand.play_val_strategy(prev_card)
        #Compare what we just played to the leading card on the table
        leading_card = self.__table.leading_card()
        checkout = self.__table.check_suggestion(to_play)
        if checkout == "correct":
            return "WIN"
        else:
            #If you get the right number...
            if checkout == "number":
                if len(self.__table.remaining_deck()) > 1:
                    self.__table.add_card(2)
                elif len(self.__table.remaining_deck()) ==1:
                    self.__table.add_card(1)
            #And if you have the right suit:
            elif checkout == "suit":
                if len(self.__table.remaining_deck()) > 0:
                    self.__table.add_card(1)
            self.__hand.remove_card(leading_card)
            self.__table.pop_card(1)
            if self.check_loss():
                return "LOSE"
            return ["Continue",to_play]

    def check_loss(self):
        if self.__hand.num_cards_remaining() == 0 or self.__table.num_cards_on_table() == 0:
            return True

    def play(self, strategy = "suits_strat"):
        status = ["Continue",1]
        prev_card = "nothing"
        while status[0] == "Continue":
            status = self.play_card(prev_card,strategy)
            prev_card = status[1]
        return status