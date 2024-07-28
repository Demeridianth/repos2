import random
import os





def roll_dice():

   min_val = 1
   max_val = 6
   roll_again = 'y'

   while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
      os.system('cls' if os.name == 'nt' else 'clear')
      print('Rolling the die...')
      dice_1 = random.randint(min_val, max_val)
      print(f'The value is: {dice_1}')

      roll_again = input('Roll Again? ')

if __name__ == '__main__':
   roll_dice()
       

       
      
      


