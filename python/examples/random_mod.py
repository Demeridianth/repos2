from random import shuffle, random, randint, randrange, choice, choices, sample, seed

people: list[str] = ['Bob', 'Tom', 'James', 'Sandra']
shuffle(people)
print(people)
# >>> ['Bob', 'Sandra', 'Tom', 'James']


value: float = random()
# value = float(random())
print(f'random() = {value}')
# >>> random() = 0.3774680787354513
# random WILL ALWAYS give a value from 0 to 1 !!!


values: list[int] = [randint(10, 20) for _ in range(5)]
# randint will include 10 and 20 !!!
print(f'randint() = {values}')
# >>> [11, 13, 12, 13, 17]


values2: list[int] = [randrange(0, 10, 2) for _ in range(5)]
# randrange will EXCLUDE 10; 2 - IS A STEP!
print(f'randrange() = {values2}')
# >>> [6, 6, 0, 6, 6]
# randrange(0, 10, 2) = will always return EVEN NUMBERS
# randrange(1, 10, 2) = will always return ODD NUMBERS


people: list[str] = ['Bob', 'Tom', 'James', 'Sandra']
print(f'choice() = {choice(people)}')
# >>> Sandra


weights: tuple = (.15, .20, .35, .30)
people: list[str] = ['Bob', 'Tom', 'James', 'Sandra']

print(f'choices() = {choices(people, k=5, weights=weights)}')
# >>> ['Bob', 'Sandra', 'Tom', 'Tom', 'Tom']
# choices will return any number of random values thorugh K=n argument
# weights are propability in which
#  {people} have a chance to be {choices}


print(sample(range(100), k=10))
# >>> [51, 76, 78, 62, 9, 86, 0, 39, 68, 18]
# k needs to be the same or less then the number of elements given

colors: list[str] = ['r', 'g', 'b']
print(sample(colors, k=5, counts=(10, 20, 5)))
# counts = how much of each element will be included in the sample
# >>> []'r', 'b', 'r', 'b', 'r']


seed(2)
# will tell the program to generate THE SAME results each time
# 2 is the number of the seed saved

print(f'{random() = }')
print(f'{randint(1, 5) = }')
print(f'{sample(range(1000), k=5) = }')
# same as print(f'random() = {random()}')
# >>> random() = 0.5941710639166189
