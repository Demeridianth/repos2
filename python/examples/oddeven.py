def f(x):
    if x % 2 == 0:
        print('even')
    else:
        print('odd')    


def odd(x):
    return x % 2 and 'odd' or 'even'



print('the sum of all even numbers:', sum(number for number in range(2, 101, 2)))