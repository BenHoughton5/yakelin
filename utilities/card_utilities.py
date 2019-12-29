from structures.card import Card

#Creates a full (jokerless) deck of cards
def create_deck(jokers = 0):
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    values = [str(x) for x in range(2,11)] + ['ace', 'jack', 'queen', 'king']
    #jokers_to_add = [Card(1,'joker') for i in range(0,jokers)]
    complete_set = [Card(value, suit) for value in values for suit in suits] #++ jokers_to_add
    return complete_set

#TODO: Do something with the jokers