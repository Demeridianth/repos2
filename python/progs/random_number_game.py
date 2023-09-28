import random
number = random.randint(1, 10)


guess = int(input('Guess a number: '))

if guess == number:
    print('you won')
else:
    print('try again')