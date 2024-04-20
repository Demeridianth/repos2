from time import sleep, perf_counter

def run_time(func, *args, **kwargs):
    print('Function start...')
    sleep(1)
    start_time = perf_counter()
    func(*args, **kwargs)
    end_time = perf_counter()
    print(f'It took {end_time - start_time: 0.02f} seconds to complete')


# without args
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
    print(result)

# test function
def switch():
    letters = ['a', 'b', 'c']
    letters.reverse()
    print(letters)


if __name__ == '__main__':
    run_time(in_cube_even, [n for n in range(10000)])


# t0 = perf_counter(); in_cube_even([n for n in range(100)]);  t1 = perf_counter()
# print(f'function took {t0 - t1} to complete')