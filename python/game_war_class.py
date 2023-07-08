from random import shuffle


CARD_SUITS = ('spades', 'hearts', 'diamonds', 'clubs')
CARD_VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')


class Card:
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        return f'{CARD_VALUES[self.value - 2]} of {CARD_SUITS[self.suit]}'
    

class Deck:
    def __init__(self) -> None:
        self.cards = []
        for i in range(len(CARD_VALUES)):
            for j in range(len(CARD_SUITS)):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
    
class Player:
    def __init__(self, name) -> None:
        self.wins = 0
        self.name = name


class Game:
    def __init__(self) -> None:
        name1 = input('player1 name ')
        name2 = input('player2 name ')
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def play_game(self):
        cards = self.deck.cards
        print('beginning War!')
        response = None
        while len(cards) >= 2 and response != 'q':
            response = input('q to quit. Any other key to play')
            player1_card = self.deck.remove_card()
            player2_card = self.deck.remove_card()
            print(f'{self.player1.name} drew {player1_card}, {self.player2.name} drew {player2_card}')
            if player1_card > player2_card:
                self.player1.wins += 1
                print(f'{self.player1.name} wins this round')
            else:
                self.player2.wins += 1
                print(f'{self.player2.name} wins this round')
        print(f'The war is over. {self.winner(self.player1, self.player2)} wins')

    def winner(self, player1, player2):
        if self.player1.wins > self.player2.wins:
            return self.player1.name
        if self.player1.wins < self.player2.wins:
            return self.player2.name
        return 'It was a tie!'
    
game = Game()
game.play_game()