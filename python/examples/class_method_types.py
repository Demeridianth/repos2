# class Myclass:
#     def method(self):
#         print('method has been called', self)

#     @classmethod
#     def class_method(cls):
#         print('class method has been called', cls)

#     @staticmethod
#     def static_method():
#         print('static method has been called')

# obj = Myclass()

# obj.method()
# Myclass.class_method()
# Myclass.static_method()
# obj.static_method()


# class Pizza:
#     def __init__(self, ingridients) -> None:
#         self.ingi = ingridients

#     def __repr__(self) -> str:
#         return f'Pizza ingridients are {self.ingi}'
    
#     @classmethod
#     def margarita(cls):
#         return cls(['mazarella', 'tomatoes'])
    
#     @classmethod
#     def priscutto(cls):
#         return cls(['chees', 'ham', 'mushrooms'])
    


# import math

# class Pizza:
#     def __init__(self, radius, ingredients):
#         self.radius = radius
#         self.ingredients = ingredients

#     def __repr__(self):
#         return (f'Pizza({self.radius!r}, '
#                 f'{self.ingredients!r})')

#     def area(self):
#         return self.circle_area(self.radius)

#     @staticmethod
#     def circle_area(r):
#         return r ** 2 * math.pi


class Dog:
    has_fur = True

    def __init__(self, name) -> None:
        self.name = name

    @classmethod
    def change_has_fur(cls, has_fur: bool):
        cls.has_fur = has_fur

fido = Dog('Fido')
snoopy = Dog('Snoopy')
