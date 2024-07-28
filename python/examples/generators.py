import sys
import re


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# for i in infinite_sequence():
#     print(i, end='')



num_squared_listed = [i ** 2 for i in range(10000)]
# print(sys.getsizeof(num_squared_listed)) 

num_squared_generated = (i ** 2 for i in range(10000))
# print(sys.getsizeof(num_squared_generated)) 



def get_even(list_of_nums):
    for i in list_of_nums:
        if i % 2 == 0:
            yield i

list_of_nums = [1, 2, 3, 8, 15, 42]

# до генератора

# print('Before generator filter: ', list_of_nums)

# после генератора

# print('Only even numbers: ', end='')
# for i in get_even(list_of_nums):
#     print(i, end=' ')






# Функция будет бесконечно генерировать
# последовательность чисел в третьей степени,
# начиная с 1


def next_in_cube():
    first_number = 1

    while True:
        yield first_number**3
        first_number += 1

# Запрашиваем у генератора и выводим ровно 15 чисел

count = 1
for number in next_in_cube():
    if count > 15:
        break
    # print(number)
    count += 1




# Этот генератор создает последовательность значений True: по одному на каждое
# найденное слово 'python'
# Также он выводит обработанные слова


def get_python(text):
    text = re.split('[., ]+', text)
    for word in text:
        # print(word)
        if word == 'python':
            yield True

text = 'There is a lot of \
        methods in python. \
        Program wont read \
        this last sentence!'

result = 'not found'

for python in get_python(text):
    result = 'found'
    break

# print('Search result: ', result)






def my_generator():
    last = 100
    while last:
        yield last
        last -= 1

for number in my_generator():
    print(number)


    













    





        



        
