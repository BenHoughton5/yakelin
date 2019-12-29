class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return str(self.value) + " of " + self.suit

    def __eq__(self,other):
        return self.value == other.value and self.suit == other.suit

    def __ne__(self, other):
        return self.value != other.value or self.suit != other.suit

