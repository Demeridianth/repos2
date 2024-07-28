import threading
import time

""" with done variable """

# done = False

# def worker():
#     counter = 0
#     while not done:
#         time.sleep(1)
#         counter += 1
#         print(counter)

# threading.Thread(target=worker).start()
# input('press enter to quit')




""" worker becomes a deamon thread = if nothing else is running, u can also quit this, it is running in the background """

# def worker():
#     counter = 0
#     while True:
#         time.sleep(1)
#         counter += 1
#         print(counter)

# threading.Thread(target=worker, daemon=True).start()
# input('press enter to quit')




""" with arguments """

def worker(text):
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        print(f'{text}: {counter}')

t1 = threading.Thread(target=worker, daemon=True, args=('abc',))
t2 = threading.Thread(target=worker, daemon=True, args=('another text',))

t1.start()
t2.start()



input('press enter to quit')
