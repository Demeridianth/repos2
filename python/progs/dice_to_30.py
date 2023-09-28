import random
import os
import time


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0

    def add_points(self, points):
        self.score += points


def roll_dice():
    min_val = 1
    max_val = 6
    dice_value = random.randint(min_val, max_val)
    return dice_value

def countdown(user_time):
    while user_time >= 0:
        mins, secs = divmod(user_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        user_time -= 1
        
        

player1_name = input('enter name: ')
player2_name = input('enter name: ')
player1 = Player(player1_name)
player2 = Player(player2_name)
roll_again = 'y'

while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Rolling the die...')


    countdown(5)
    player1_roll = roll_dice()
    player1.add_points(player1_roll)
    print(f'{player1.name} has {player1.score}')

    countdown(5)
    player2_roll = roll_dice()
    player2.add_points(player2_roll)
    print(f'{player2.name} has {player2.score}')

    if player1.score >= 30:
        print(f'game over: {player1_name} has won')
        break
    elif player2.score >= 30:
        print(f'game over: {player2_name} has won')
        break

    roll_again = input('Roll Again? ')




    



