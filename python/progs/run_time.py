from time import sleep, perf_counter

def run_time(func, *args, **kwargs):
    print('Function start...')
    sleep(1)
    start_time = perf_counter()
    func(*args, **kwargs)
    end_time = perf_counter()
    print(f'It took {end_time - start_time: 0.2f} seconds to complete')

# def run_time(func):
#     print('go...')
#     sleep(0.5)
#     start_time = perf_counter()
#     func()
#     end_time = perf_counter()
#     print(f'function took {end_time - start_time:0.2f} to complete')

# test function
def in_cube_even(nums):
    result = [n**2 for n in nums if n % 2 == 0]
    return result

# test function
def switch():
    letters = ['a', 'b', 'c']
    letters.reverse()
    print(letters)

if __name__ == '__main__':
    run_time(switch)