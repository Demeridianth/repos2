from random import shuffle

CARD_SUITS = ('spades', 'hearts', 'diamonds', 'clubs')
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 10
}

class Card:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self) -> str:
        return str(CARD_VALUES[self.value])
    
class Deck:
    def __init__(self):
        self.cards = [Card(value) for value in CARD_VALUES]
        shuffle(self.cards)
    
    def draw_card(self):
        if not self.cards:
            return None
        return self.cards.pop()
    
class Player:
    def __init__(self, name):
        self.name = name
        self._hand = 0
    
    @property
    def hand(self):
        return self._hand
    
    def add_card(self, card):
        self._hand += card
    
class GameUI:
    @staticmethod
    def name_players():
        player1 = GameUI.get_user_input('player1 name: ')
        player2 = GameUI.get_user_input('player2 name: ')
        return player1, player2
    
    @staticmethod
    def get_user_input(message, converter=str):
        return converter(input(message))
    

player1 = Player('Mike')
player2 = Player('Felix')

deck = Deck()

players = [player1, player2]
is_players_done = False

while not is_players_done:
    for player in players:
        decision = input(f'{player.name}? Take a card? (y/n/q): ')
        
        if decision == 'y':
            card = deck.draw_card()
            player.add_card(card)
            print(f'{player.name} has {player.hand} points')
        elif decision == 'n':
            continue
        elif decision == 'q':
            is_players_done = True
            break