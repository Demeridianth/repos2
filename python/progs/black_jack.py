from random import shuffle


CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 10
}


class Deck:
    def __init__(self) -> None:
        self._cards = [value for value in CARD_VALUES.values() for _ in range(4)]
        shuffle(self._cards)

    def draw_card(self):
        if not self._cards:
            return None
        return self._cards.pop()

    
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = 0

    def add_card_to_hand(self, card):
        self.hand += card


class GameUI:
    @staticmethod
    def get_players_names():
        player1 = GameUI._get_user_input('player1 name: ')
        player2 = GameUI._get_user_input('player2 name: ')
        return player1, player2
    
    @staticmethod
    def get_players_decision():
        players_decision = GameUI._get_user_input('Take a card? (y/n/q): ')
        return players_decision

    @staticmethod
    def _get_user_input(message, converter=str):
        return converter(input(message))
    

player1_name, player2_name = GameUI.get_players_names()
player1 = Player(player1_name)
player2 = Player(player2_name)
deck = Deck()
is_player_1_done = False
is_player_2_done = False

while not (is_player_1_done and is_player_2_done):
    if not is_player_1_done:
        player1_decision = GameUI.get_players_decision()
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
        player2_decision = GameUI.get_players_decision()
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

# перебор
if player1.hand > 21:
    print(f'{player2.name} WON!')
elif player2.hand > 21:
    print(f'{player1.name} WON!')

# ничья
elif player1.hand == player2.hand:
    print('It is a TIE!!!')

# у кого больше очков
elif player1.hand > player2.hand:
    print(f'{player1.name} WON!')
else:
    print(f'{player2.name} WON!')
    
