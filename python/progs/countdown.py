import time
import threading




done = False


### without the thread
def countdown(user_time):
   while user_time >= 0 and not done:
      mins, secs = divmod(user_time, 60)
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end='\r')
      time.sleep(1)
      user_time -= 1
### without the thread


thread_countdown = threading.Thread(target=countdown, args=(10,))

if __name__ == '__main__':
   # user_time = int(input("Enter a time in seconds: "))
   thread_countdown.start()
   input('press enter to stop\n')
   done = True