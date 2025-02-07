"""args"""
def order_pizza(size, *args):
    print(f'you ordered a {size} pizza with these toppings: {args} ')
    # for arg in args:
    #     print(arg)

order_pizza('large', 'olives', 'pepperoni')
# >>> you ordered a large pizza with these toppings: 
# olives
# pepperoni


nums = [1, 2, 3, 4]
# print(*nums)
# >>> 1 2 3 4


def unpacked(lst, *args):
    result = [n for n in args]
    return lst + result

# print(test([1, 2, 3, 4], 5, 6, 7))



"""kwargs"""

person = {'name': 'Bob', 'age': 30, 'position': 'manager'}

def iterate(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}\n')

iterate(**person)






def details(**kwargs):
    print('Details of the order are:')
    for key, value in kwargs.items():
        print(f' -{key}: {value}')


details(order=True, tip=5)


def name_list(proffesion, **kwargs):
    print(f'list of today {proffesion} workers:')
    for name, surname in kwargs.items():
        print(f'{name} {surname}')

name_list('constuction', Mike='Johnson', Gary='Wild')