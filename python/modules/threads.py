from threading import Thread 
import threading
from time import sleep, perf_counter
import time


""" new_thread = Thread(target=function, args=tuple) """

# The Thread() accepts many parameters. The main ones are:

# target: specifies a function (fn) to run in the new thread.
# args: specifies the arguments of the function (fn). The args argument is a tuple.





""" task in one second """
# def task():
#     print('Start task...')
#     sleep(1)
#     print('done')

# start_time = perf_counter()

# # creating 2 new threads
# thread1 = Thread(target=task)
# thread2 = Thread(target=task)

# # start threads
# thread1.start()
# thread2.start()

# # wait for the threads to complete
# thread1.join()
# thread2.join()

# end_time = perf_counter()

# print(f'it took {end_time- start_time: 0.2f} second(s) to complete')



""" we will give each task id and an argument to thread """
# def task(id):
#     print(f'start the task {id}...')
#     sleep(1)
#     print(f'the task {id} completed')

# start_time = perf_counter()

# # create 10 threads
# threads = []
# for n in range(1, 11):
#     t = Thread(target=task, args=(n, ))
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

# end_time = perf_counter()

# print(f'it took {end_time- start_time: 0.2f} second(s) to complete')



""" more practical example """
""" string replacement without threads """
# def replace(filename, string, new_string):
#     print(f'Processing the file {filename}')
#     # get the contents of the file
#     with open(filename, 'r') as f:
#         content = f.read()

#     # replace str with a new str
#     content = content.replace(string, new_string)

#     # write data to file
#     with open(filename, 'w') as f:
#         f.write(content)

# def main():
#     filenames = [
#         'temp/test1.txt',
#         'temp/test2.txt',
#         'temp/test3.txt',
#         'temp/test4.txt',
#         'temp/test5.txt',
#         'temp/test6.txt',
#         'temp/test7.txt',
#         'temp/test8.txt',
#         'temp/test9.txt',
#         'temp/test10.txt',
#     ]

#     for filename in filenames:
#         replace(filename, 'ids', 'id')


# if __name__ == '__main__':
#     start_time = perf_counter()

#     main()

#     end_time = perf_counter()
#     print(f'it took {end_time - start_time: 0.2f} second(s) to complete')




""" string replacement with threads """
# def replace(filename, string, new_string):
#     print(f'Processing the file {filename}')
#     with open(filename, 'r') as f:
#         content = f.read()
#     content = content.replace(string, new_string)
#     with open(filename, 'w') as f:
#         f.write(content)

# def main():
#     filenames = [
#         'temp/test1.txt',
#         'temp/test2.txt',
#         'temp/test3.txt',
#         'temp/test4.txt',
#         'temp/test5.txt',
#         'temp/test6.txt',
#         'temp/test7.txt',
#         'temp/test8.txt',
#         'temp/test9.txt',
        # 'temp/test10.txt',
    # ]

#     # creating threads
#     threads = [Thread(target=replace, args=(filename, 'ids', 'id')) for filename in filenames]

#     # starting the threads
#     for thread in threads:
#         thread.start()

#     # waiting for the threads to complete
#     for thread in threads:
#         thread.join()

    
# if __name__ == '__main__':
#     start_time = perf_counter()

#     main()

#     end_time = perf_counter()
#     print(f'it took {end_time - start_time: 0.2f} second(s) to complete')




"""FROM YT"""



""" with done variable """

done = False

def worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)

threading.Thread(target=worker).start()
input('press enter to quit')
done = True




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

# def worker(text):
#     counter = 0
#     while True:
#         time.sleep(1)
#         counter += 1
#         print(f'{text}: {counter}')

# t1 = threading.Thread(target=worker, daemon=True, args=('abc',))
# t2 = threading.Thread(target=worker, daemon=True, args=('another text',))

# t1.start()
# t2.start()



# input('press enter to quit')