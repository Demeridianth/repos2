from random import shuffle


CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 10}

class Card:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if self.value < other.value:
            return True
        return False
    
    def __gt__(self, other):
        if self.value > other.value:
            return True
        return False