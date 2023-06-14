# class Employee:
#     def __init__(self, name, surname):
#         self.first_name = name
#         self.last_name = surname
#         self.salary = 1000

#     def increase_salary(self):
#         self.salary += 100

#     def decrease_salary(self):
#         self.salary -= 100

# bob = Employee('Bob', 'Jones')
# sam = Employee('Sam', 'Heckley')


# class Animal:  
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
#         self.legs_count = 4

#     def make_sound(self):
#         print('unknown sound')


# class Cat(Animal):
#     pass
    

# class Dog(Animal):
#     def make_sound(self):
#         print('Woof')    


# tom = Cat('tom', 4)
# goofy = Dog('goofy', 6)

# print(tom.age)
# tom.make_sound()
# goofy.make_sound()


# class Mammal:
#     def __init__(self, color, has_tail=True, legs_count=4, sound=None) -> None:
#         self.color = color
#         self.has_tail = has_tail
#         self.legs_count = legs_count

#     def make_sound(self):
#         if self.sound is not None:
#             print(self.sound)
#         else:
#             print('')


# class PetMammal(Mammal):
#     def __init__(self, name, color, has_tail=True, legs_count=4, sound=None) -> None:
#         self.name = name
#         super().__init__(color, has_tail, legs_count, sound)


# class Cat(Mammal):
#     def make_sound(self) -> None:
#         print(f'{self.color} cat says ', end='')
#         super().make_sound()


# class PetCat(PetMammal):
#     def make_sound(self) -> None:
#         print(f'{self.name} says ', end='')
#         super().make_sound()


# class Dog(Mammal):
#     def make_sound(self) -> None:
#         print(f'{self.color} dog says ', end='')
#         super().make_sound()


# class PetDog(PetMammal):
#     def make_sound(self) -> None:
#         print(f'{self.name} says ', end='')
#         super().make_sound()



# class Tiger:
#     interests = ['sleeping', 'eating']

#     def __init__(self, name):
#         self.name = name


# bob = Tiger('Bob')
# print(bob.interests)
# bob.interests = ['doing nothing']
# print(bob.interests)

# print('---')

# maddy = Tiger('Madelyn')
# maddy.interests = ['sleeping', 'eating', 'playing']
# print(Tiger.interests)
# print(maddy.interests)

# print('---')
# Tiger.interests = []

# simon = Tiger('Simon')
# print(simon.interests)\


# class Numbers:
#     def __init__(self) -> None:
#         self._data = []

#     def add(self, value):
#         self._data.append(value)

#     def get(self, index):
#         return self._data[index]
    
#     def get_length(self):
#         return len(self._data)
    
#     def __len__(self):
#         return len(self._data)
    



# class NumbersIter:
#     def __init__(self, instance) -> None:
#         self.instance = instance
#         self.position = - 1

#     def __next__(self):
#         self.position += 1
#         if self.position < len(self.instance):
#             return self.instance[self.position]
#         else:
#             raise StopIteration

# class Numbers:
#     def __init__(self) -> None:
#         self._data = [1, 2, 3, 4]

#     def __len__(self):
#         return len(self._data)
    
#     def __getitem__(self, index):
#         return self._data[index]
    
#     def __setitem__(self, index, value):
#         self._data[index] = value

#     def __str__(self):
#         return str(self._data)
    
#     def __repr__(self):
#         return self._data
    
#     def __iter__(self):
#         return NumbersIter(self)




class NumbersIterator:
    def __init__(self, numbers_instance: 'Numbers') -> None:
        self._numbers_to_iterate = numbers_instance
        self._position = -1

    def __next__(self) -> int:
        self._position += 1
        if self._position < len(self._numbers_to_iterate):
            return self._numbers_to_iterate.get(self._position)
        else:
            raise StopIteration


class Numbers:
    def __init__(self) -> None:
        self._data = [1, 2, 3, 4]

    def __getitem__(self, index: int) -> int:
        return self._data[index]

    def __setitem__(self, index: int, value: int) -> None:
        self._data[index] = value

    def __iter__(self):
        # Если метода __contains__ нет, то код:
        # numbers = Numbers()
        # value in numbers
        # вызовет __iterator__
        # и при помощи полученного итератора переберет все значения
        print('inside __iter__')
        return NumbersIterator(self)

    def __contains__(self, value: int) -> bool:
        # Если метод __contains__ есть, то код:
        # numbers = Numbers()
        # value in numbers
        # вызовет его
        print('inside __contains__')
        return value in self._data

    def __len__(self) -> int:
        return len(self._data)

    def __str__(self) -> str:
        # Показать строковое представление объекта для человека
        return str(self._data)

    def __repr__(self) -> str:
        # От representation - показать "техническое" строковое представление для программиста
        return f'<Объект Numbers c числами {self._data}>'