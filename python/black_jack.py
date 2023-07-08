from random import shuffle


CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 10
}

    
class Deck:
    def __init__(self) -> None:
        self.cards = [value for key, value in CARD_VALUES.items() for suit in range(4)]
        shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            return None
        return self.cards.pop()

    
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = 0

    def add_card_to_hand(self, card):
        self.hand += card


class GameUI:
    @staticmethod
    def get_players_names():
        player1 = GameUI.get_user_input('player1 name: ')
        player2 = GameUI.get_user_input('player2 name: ')
        return player1, player2
    
    @staticmethod
    def get_user_input(message, converter=str):
        return converter(input(message))
    

# player1, player2 = GameUI.get_players_names()

player1 = Player('Mike')
player2 = Player('Felix')
deck = Deck()
is_player_1_done = False
is_player_2_done = False


while not (is_player_1_done and is_player_2_done):
    if not is_player_1_done:
        player1_decision = GameUI.get_user_input(f'{player1.name}? Take a card? (y/n/q): ')
        if player1_decision == 'y':
            player1_card = deck.draw_card()
            player1.add_card_to_hand(player1_card)
            print(f'{player1.name} has {player1.hand} points')
        if player1.hand > 21:
            break
        elif player1_decision == 'n' or player1.hand == 21:
            is_player_1_done = True
        elif player1_decision == 'q':
            break
    
    if not is_player_2_done:
        player2_decision = GameUI.get_user_input(f'{player2.name}? Take a card? (y/n/q): ')
        if player2_decision == 'y':
            player2_card = deck.draw_card()
            player2.add_card_to_hand(player2_card)
            print(f'{player2.name} has {player2.hand} points')
        if player2.hand > 21:
            break
        elif player2_decision == 'n' or player2.hand == 21:
            is_player_2_done = True
        elif player2_decision == 'q':
            break

if player1.hand > 21:
    print(f'{player2.name} WON!')
elif player2.hand > 21:
    print(f'{player1.name} WON!')
elif player1.hand == player2.hand:
    print('It is a TIE!!!')
elif player1.hand > player2.hand:
    print(f'{player1.name} WON!')
else:
    print(f'{player2.name} WON!')
    
