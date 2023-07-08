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
        self.cards = [Card(value) for value in CARD_VALUES for _ in range(len(CARD_SUITS))]
        shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            return None
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = 0


class GameUI:
    @staticmethod
    def name_players():
        player1 = GameUI._get_user_input('player1 name: ')
        player2 = GameUI._get_user_input('player2 name: ')
        return player1, player2

    @staticmethod
    def _get_user_input(message, converter=str):
        return converter(input(message))


if __name__ == '__main__':
    deck = Deck()
    ui_function = GameUI()
    player1_name, player2_name = ui_function.name_players()
    player1 = Player(player1_name)
    player2 = Player(player2_name)

    while True:
        player1_card = deck.draw_card()
        print(player1_card)
        player1.hand += int(player1_card.value)
        print(player1.hand)