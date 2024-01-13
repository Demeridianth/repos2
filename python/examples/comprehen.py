""" comprehension """
import random
import timeit


# FORMULA -  new_list = [expression for member in iterable]

# calculate the price after tax for a list of transactions

# for loop
transactions = [1.09, 23.56, 57.84, 4.56, 6.78]
tax_rate = .08
final_prices = []
for trn in transactions:
    final_prices.append(trn * (1 + tax_rate))

# mapping
def taxation_function(transaction):
    return transaction * (1 + tax_rate)
final_prices_map = list(map(taxation_function, transactions))
# >>> [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]

# list comprehension
final_prices_compr = [taxation_function(transaction) for transaction in transactions]
# >>> [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]


# addind conditions
# FORMULA - new_list = [expression for member in iterable (if conditional)]

sentence = 'the rocker has left for mars'
vowels = [i for i in sentence if i in 'aeiou']

# with filter function
sentence = 'The rocket, who was named Ted, came back \ from Mars because he missed his friends.'
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
consonants = [i for i in sentence if is_consonant(i)]




# conditions with multiple possible outputs
# new_list = [expression (if conditional) for member in iterable]
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

# result = []
# for price in original_prices:
#     if price > 0:
#         result.append(price) 
#     else:
#         0
    
prices = [price if price > 0 else 0 for price in original_prices]

# with filter function
def get_price(price):
    # if price > 0:
    #     return price
    # else:
    #     return 0
    return price if price > 0 else 0
prices_filtered = [get_price(price) for price in original_prices]



# set comprehension

quote = 'life, uh, finds a way'
unique_vowels = {i for i in quote if i in 'aeiou'}
# Your set comprehension outputs all the UNIQUE vowels it found in quote


# dict comprehension
squares = {i: i * i for i in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# To create the squares dictionary, you use curly braces ({}) as well as a key-value pair (i: i * i) in your expression.



# using Walrus operator

def get_weather_data():
    return random.randrange(90, 110)
hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]

# hot_temps = []
# for _ in range(20):
#     temp = get_weather_data()
#     if temp >= 100:
#         hot_temps.append(temp)

# print(hot_temps)



# Nester Comprehensions
cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
temps = {city: [0 for _ in range(7)] for city in cities}

# temps = {}
# for city in cities:
#     temps[city] = []
#     for _ in range(7):
#         temps[city].append(0)


matrix = [[i for i in range(5)] for _ in range(6)]

# matrix = []
# nums = []
# for i in range(5):
#     nums.append(i)
# for _ in range(6):
#     matrix.append(nums)



matrix = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
]
flat = [num for row in matrix for num in row]

# flat = []
# for row in matrix:
#     for num in row:
#         flat.append(num)



# Choose Generators for Large Datasets

# list comprehension
# square_sum = sum([i * i for i in range(1000)])

# generator
# large_square = sum(i * i for i in range(100000000))


import random
import timeit
TAX_RATE = .08
txns = [random.randrange(100) for _ in range(100000)]
def get_price(txn):
    return txn * (1 + TAX_RATE)

def get_prices_with_map():
    return list(map(get_price, txns))

def get_prices_with_comprehension():
    return [get_price(txn) for txn in txns]

def get_prices_with_loop():
    prices = []
    for txn in txns:
        prices.append(get_price(txn))
    return prices

print(timeit.timeit(get_prices_with_map, number=100))

print(timeit.timeit(get_prices_with_comprehension, number=100))

print(timeit.timeit(get_prices_with_loop, number=100))



























    
    

    


