import random
import os
import time
from threading import Thread
import pyinputplus


""" 2 players roll the dice, whoever gets to 30 points first WINS... Also if a player doesnt roll in 10 seconds he loses"""
"""in order to roll press R and then ENTER, in order to start another round press Y"""


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
    while user_time >= 0 and not done:
        mins, secs = divmod(user_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        user_time -= 1
        if user_time == 0:
            pass
        

player1_name = input('enter name: ')
player2_name = input('enter name: ')
player1 = Player(player1_name)
player2 = Player(player2_name)
roll_again = 'y'


# function creating threads
# def new_thread():
#     thread = Thread(target=countdown, args=(10,)).start()
#     return thread


if __name__ == '__main__':
    while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
        # clear terminal on each iteration
        os.system('cls' if os.name == 'nt' else 'clear')

        
        """ Player 1 """

        print(f'Hurry up {player1_name}')
        done = False
        thread = Thread(target=countdown, args=(10,))
        thread.start()
        inp = pyinputplus.inputStr(prompt = "press R and ENTER to roll:  \n", default = 'you_were_too_slow', timeout = 10)
        if inp == 'you_were_too_slow':
            print(f'you_were_too_slow! {player2_name} has WON')
            break
        done = True
        thread.join()
        player1_roll = roll_dice()
        player1.add_points(player1_roll)
        print(f'{player1.name} has {player1.score}')


        """ Player 2 """

        print(f'Hurry up {player2_name}')
        done = False
        thread = Thread(target=countdown, args=(10,))
        thread.start()
        inp = input(prompt = "press R and ENTER to roll:  ")
        if inp == 'you_were_too_slow':
            print(f'you_were_too_slow! {player1_name} has WON')
            break
        done = True
        thread.join()
        player2_roll = roll_dice()
        player2.add_points(player2_roll)
        print(f'{player2.name} has {player2.score}')


        """ Victory conditions """

        if player1.score >= 30:
            print(f'game over: {player1_name} has won')
            break
        elif player2.score >= 30:
            print(f'game over: {player2_name} has won')
            break

        roll_again = input('Roll Again? ')




    



