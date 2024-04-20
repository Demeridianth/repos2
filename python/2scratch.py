import sys


numbers = [n for n in range(1, 1000000)]
nums = list(range(1, 1000000))
gen_nums = list(n for n in range(1, 1000000))


print(sys.getsizeof(numbers))
print(sys.getsizeof(nums))
print(sys.getsizeof(gen_nums))



