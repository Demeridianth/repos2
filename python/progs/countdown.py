import time
import threading



done = False


### without the thread
def countdown(user_time):
   while user_time > 0 and not done:
      
      mins, secs = divmod(user_time, 60)
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end='\r')
      time.sleep(1)
      user_time -= 1
      
      
      
### with the thread, doesnt work



# if __name__ == '__main__':
#    while not done:
#       done = False
#       thread_countdown = threading.Thread(target=countdown, daemon=True, args=(5,))
#       thread_countdown.start()
#       choice = input('press enter')
#       done = True
      
countdown(10)
      