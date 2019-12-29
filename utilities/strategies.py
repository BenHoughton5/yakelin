from structures.card import Card
from collections import Counter
import random

#suit_first checks all of the cards which haven't been uncovered and takes the most common suit.  It then takes the number which has appeared least so far out of the possible ones
def suit_first(cards_playable):
    suits = [x.suit for x in cards_playable]
    most_common_suit = max(set(suits), key=suits.count)

    numbers_for_suit = [x.value for x in cards_playable if x.suit == most_common_suit]
    numbers_overall = [x.value for x in cards_playable]

    val_to_play = find_most_frequent(numbers_overall, numbers_for_suit)

    return Card(val_to_play,most_common_suit)

#num_first checks all of the cards which haven't been uncovered and takes the most common number.  It then takes the suit which has appeared least so far out of the possible ones
def num_first(cards_playable):
    numbers = [x.value for x in cards_playable]
    most_common_number = max(set(numbers), key=numbers.count)

    suits_for_number = [x.suit for x in cards_playable if x.value == most_common_number]
    suits_overall = [x.suit for x in cards_playable]

    suit_to_play = find_most_frequent(suits_overall, suits_for_number)

    return Card(most_common_number,suit_to_play)


#Finds the most frequently occuring number from one list in another list
def find_most_frequent(sublist, tocheckin):
    frequent_val = max(set(sublist), key=sublist.count)
    if frequent_val in tocheckin:
        return frequent_val
    else:
        return find_most_frequent([x for x in sublist if x != frequent_val], tocheckin)