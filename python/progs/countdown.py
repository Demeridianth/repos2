import time
# from pynput.keyboard import Key, Controller
from sshkeyboard import listen_keyboard
import keyboard

# do i need Virtual Network Computing server??


def press(key):
   print(f'{key}')

def countdown(user_time):
   while user_time >= 0:
      mins, secs = divmod(user_time, 60)
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end='\r')
      time.sleep(1)
      user_time -= 1
   
      
      
         

      

if __name__ == '__main__':
   # user_time = int(input("Enter a time in seconds: "))
   countdown(10)