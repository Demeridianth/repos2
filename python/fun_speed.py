from time import perf_counter, sleep
import O_of_one


def run_time(function, *args, **kwargs):
    print('Function start...')
    sleep(1)
    start_time = perf_counter()
    function(*args, **kwargs)
    end_time = perf_counter()
    print(f'your function took {end_time - start_time: 0.04f} to run')


# get all even numbers squared | function with an argument
def in_cube_even(nums):
    result = [n**2 for n in nums if n % 2 == 0]
    return result

# simple function without any arguments
def simple_function():
    sleep(1)
    print('Simple function done')


def main():
    run_time(in_cube_even, range(10*1000))
    run_time(simple_function)


if __name__ == '__main__':
    main()


# as a wrapper
def time_logger(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        # sleep(1)
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f'it took {end - start: 0.04f} to compute your function')
        return result
    return wrapper