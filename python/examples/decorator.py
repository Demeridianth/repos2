#decorator


#1
# def my_func():
#     print('this is inside')

# def decorator(func):
#     def wrapper():
#         print('before wrap')
#         func()
#         print('after wrap')
#     return wrapper

# my_func = decorator(my_func)

# print(my_func())


#2

# def decorator(func):
#     def wrapper():
#         print('before wrap')
#         func()
#         print('after wrap')
#     return wrapper

# @decorator
# def my_func():
#     print('some other message')



                
#3 datetime
        

# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#             pass 
#     return wrapper


# @not_during_the_night
# def my_func():
#     print('only during day time')


# 4 return wrapped function twice

def do_it_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

@do_it_twice
def my_func():
    print('text twice')

print(my_func())
