from typing import Any
import random
# class Orange:
#     def __init__(self, weight, color, mold):
#         self.color = color
#         self.weight = weight
#         self.mold = mold

# orange = Orange(10, 'orange', 'moldy')


# print(orange.weight)


# class Table():
#     def __init__(self, name, shape, color ) -> None:
#         self.name = name 
#         self.color = color
#         self.shape = shape
#         self.material = 'wood'

# table1 = Table('woodsman123', 'round', 'brown')
# print(table1.name)
# print(table1.shape)





# class Apple():
#     def __init__(self, name, color) -> None:
#         self.name = name
#         self.color = color
#         self.mold = 0

#     def rot(self, days, temperature):
#         self.mold = days * (temperature * 1)

# apple = Apple('apple', 'green')
# print(apple.color)
# apple.rot(5, 20)
# print(apple.mold)




# class Orange:
#     def __init__(self):
#         self.color = 6
#         self.weight = 10
#         self.mold = 0

#     def rot(self, days, temperature):
#         self.mold = days * (temperature * .1)

# orange = Orange()
# print(orange.mold)
# orange.rot(10, 98)
# print(orange.mold)





# class Sofa:
#     def __init__(self, color, weight, size):
#         self.color = color
#         self.weight = weight
#         self.size = size
    
#     def print_sofa(self):
#         print(self.color)
#         print(self.weight)
#         print(self.size)

#     def aging(self, years):
#         self.weight -= 0.5 * years



# sofa = Sofa('white', 100, '3x2')
# sofa.print_sofa()
# sofa.aging(5)
# sofa.print_sofa()





# class Employee():
#     def __init__(self, name, surname, salary):
#         self.name = name
#         self.surname = surname
#         self.salary = salary

#     def print_employee(self):
#         print(self.name)
#         print(self.surname)
#         print(self.salary)

#     def increase_salary(self):
#         self.salary += 100

# bob = Employee('Bob', 'Smith', 1000)
# bob.print_employee()
# bob.increase_salary()
# bob.print_employee()



# class Metal():
#     def __init__(self, weight, purity):
#         self.weight = weight
#         self.purity = purity
        

#     def cost_dependency(self):
#         self.cost = 20 * self.purity

# iron = Metal(200, 100)
# iron.cost_dependency()
# print(iron.cost)



# class Furniture():
#     def __init__(self, name, color, types) -> None:
#         self.name = name 
#         self.color = color
#         self.types = types

#     def cost_dependency(self):
#         self.cost = self.types * 1.5


# closet = Furniture('closet', 'black', 2)
# closet.cost_dependency()
# print(closet.cost)


######################################################







# class Adult:
#     def __init__(self, name, height, weight, eye_color) -> None:
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.eye_color = eye_color

#     def print_name(self):
#         print(self.name)

# Tom = Adult('Tom', 6, 150, 'brown')


# class Kid(Adult):
#     def print_cartoon(self, favorite_cartoon):
#         print(f"{self.name}'s favorite cartoon is {favorite_cartoon}")

# child = Kid('Timmy', 4, 50, 'blue')
# print(child.name)
# print(child.height)
# print(child.weight)
# print(child.eye_color)
# child.print_cartoon('Duck Tales')
    




# class Country():
#     def __init__(self, name, size, population, language):
#         self.name = name
#         self.size = size
#         self.population = population
#         self.language = language

#     def print_info(self):
#         print(f'{self.name} is {self.size} in size, its population is {self.population} and the official language is {self.language}')


# class Russia(Country):
#     pass


# class Latvia(Country):
#     pass

# russia = Russia('Russia', '17.1 million km²', '143 million', 'Russia')
# russia.print_info()


# latvia = Latvia('Latvia', '64,589 km²', '1.884 million', 'Latvian')
# latvia.print_info()




# class Iterator:
#     def __init__(self, item_to_iterate):
#         self.item_to_iterate = item_to_iterate
#         self.position = - 1

#     def __next__(self):
#         self.position += 1
#         if self.position < len(self.item_to_iterate):
#             return self.item_to_iterate[self.position]
#         else:
#             raise StopIteration



# class VideoGames():
#     def __init__(self, name, genre, rating):
#         self.name = name
#         self.genre = genre
#         self.rating = rating
#         self.list_action = []
#         self.list_shooter = []


#     def add_to_list(self, name):
#         if self.genre == 'action':
#             self.list_action.append(name)
#         if self.genre == 'shooter':
#             self.list_shooter.append(name)


#     def __iter__(self):
#         return Iterator(self)

#     def __setitem__(self, index, value):
#         self.list_action[index] = value

# metal = VideoGames('metal gear', 'action', 9.0)
# metal.add_to_list(metal)
# spider = VideoGames('spiderman', 'action', 8.0)
# spider.add_to_list(spider.name)
# print(metal.list_action)
# for g in metal.list_action:
#     print(g)


###########################################################




# class Dog():
#     def __init__(self, name, breed, owner) -> None:
#         self.name = name
#         self.breed = breed
#         self.owner = owner


# class Person():
#     def __init__(self, name) -> None:
#         self.name = name


# mick = Person('Tom SMith')
# dog = Dog('Scooby', 'Doghoud', mick.name)
# print(dog.owner)





# class Car():
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model


# class Mustang():
#     def __init__(self, name) -> None:
#         self.name = name


# must = Mustang('Mustang')
# ford = Car('Ford', must.name)
# print(ford.model)





# class Construct():
#     def __init__(self, name, job ) -> None:
#         self.name = name
#         self.job = job

# class Operator():
#     def __init__(self, job_description) -> None:
#         self.job_despription = job_description

# worker = Operator('engineer')
# proffesional = Construct('Bob', worker.job_despription)
# print(proffesional.name)



########################################################

# class Iterator:
#     def __init__(self, item) -> None:
#         self.item = item
#         self.position = - 1

#     def __next__(self):
#         self.position += 1
#         if self.position < len(self.item):
#             return self.item(self.position)
#         else:
#             raise StopIteration

# class Tiger():
    

#     def __init__(self, name) -> None:
#         self.name = name
#         self.interests = ['sleeping', 'eating', 'swimming']
#     def __getitem__(self, index):
#         return self.interests[index]
    
#     def __setitem__(self, index, value):
#         self.interests[index] = value

#     def __iter__(self):
#         return Iterator(self)
    
#     def __len__(self):
#         return len(self.interests)
    
#     def __repr__(self):
#         return self.interests

# connor = Tiger('Connor')
# print(connor.interests)
# print(connor.name)


        
    

# class Person():
#     day_schedule = ['wake up', 'breakfast', 'work', 'go home', 'dinner', 'sleep']

#     def __init__(self, name) -> None:
#         self.name = name

#     def __setitem__(self, index, value):
#         self.day_schedule[index] = value

#     def __iter__(self):
#         Iterator(self)

# mike = Person('Mike')
# print(mike.name)
# mike.day_schedule[0] = 'dont wake up'
# print(mike.day_schedule)
# for n in mike.day_schedule:
#     print(n)




################################################################



# class Mammal():
#     def __init__(self, name) -> None:
#         self.name = name
#         self.hunger = 100
#         self.tired = 100

#     def print_result(self, amount, action):
#         print(f'{self.name} {action} hoursd by {amount}')

#     def eat(self, hours):
#         self.hunger -= hours
#         self.print_result(hours, 'hunger') 
    
#     def sleep(self, hours):
#         self.tired -= hours
#         self.print_result(hours, 'tiredness')


# class Dolphin(Mammal):
#     pass


# class Tiger(Mammal):
#     def sleep(self, hours):
#         self.tired -= hours
#         print('The tiger is really tired')


# dolphin = Dolphin('dolphin')
# dolphin.eat(10)
# dolphin.sleep(10)

# tiger = Tiger('tiger')
# tiger.eat(10)
# tiger.sleep(10)






# class Car():
#     def __init__(self, name, average, tank) -> None:
#         self.name = name
#         self.average = average
#         self.tank = tank

#     def print_result(self):
#         print(f"{self.name}' tank now has {self.tank} of fuel")

#     def drive(self, distance):
#         self.tank -= self.average * distance / 100
#         self.print_result()


# class Mustang(Car):
#     pass


# class Vaz(Car):
#     pass


# ford_mustang = Mustang('Ford Mustang', 15, 50)
# ford_mustang.drive(20)

# vaz = Vaz('Zhiguli', 10, 40)
# vaz.drive(20)




# class Employee():
#     def __init__(self, name) -> None:
#         self.name = name
#         self.work_day = 8
#         self.stamina = 100

#     def print_day(self, measure, quantity):
#         print(f"{self.name}'{measure} is now {quantity}")

#     def work(self, hours):
#         self.work_day -= hours
#         self.stamina -= hours * 10
#         self.print_day('work day', self.work_day)
#         self.print_day('stamina', self.stamina)


# class Jane(Employee):
#     pass


# class Sarah(Employee):
#     def work(self, hours):
#         self.work_day -= hours
#         self.stamina -= hours * 15
#         self.print_day('work day', self.work_day)
#         self.print_day('stamina', self.stamina)
#         print('Sarah hates her job')


# jane = Jane('Jane')
# sarah = Sarah('Sarah')
# jane.work(5)
# sarah.work(5)
    

# class Tiger:
#     interests = ['sleeping', 'eating']

#     def __init__(self, name):
#         self.name = name


# bob = Tiger('Bob')
# print(bob.interests)
# Tiger.interests = []
# print(bob.interests)
# bob.interests = ['doing nothing']
# print(bob.interests)

# print('---')

# maddy = Tiger('Madelyn')
# maddy.interests = ['sleeping', 'eating', 'playing']
# print(maddy.interests)

# print('---')
# Tiger.interests = []

# simon = Tiger('Simon')
# print(simon.interests)
# print(bob.interests)



###################################################################




# class Mammal:
#     def __init__(self, color, legs_count = 4, has_tale = True, sound=None):
#         self.sound = sound
#         self.color = color
#         self.legs_count = legs_count
#         self.has_tale = has_tale

#     def make_sound(self):
#         if self.sound is not None:
#             print(self.sound)
#         else:
#             print('no sound')
    

# class PetMammal(Mammal):
#     def __init__(self, name, color, legs_count = 4, has_tale = True, sound=None):
#         self.name = name
#         super().__init__(color, legs_count, has_tale, sound)


# class PetCat(PetMammal):
#     def make_sound(self):
#         print(f'{self.name} sais ', end='')
#         super().make_sound()


# class PetDog(PetMammal):
#     def make_sound(self):
#         print(f'{self.name} sais ', end='')
#         super().make_sound()


# class Cat(Mammal):
#     def make_sound(self):
#         print(f'{self.color} sais ', end='')
#         super().make_sound()

# class Dog(Mammal):
#     def make_sound(self):
#         print(f'{self.color} sais ', end='')
#         super().make_sound()


# cat = Cat('white')
# cat.make_sound()


# pet_cat = PetCat('timmy', 'white')
# pet_cat.make_sound()


# class Iterator:
#     def __init__(self, item) -> None:
#         self.item = item
#         self.position = - 1

#     def __next__(self):
#         self.position += 1
#         if self.position < len(self.item):
#             return self.item[self.position]
#         else:
#             raise StopIteration


# class Food:
#     def __init__(self, name, price) -> None:
#         self.name = name
#         self.price = price
#         self.list1 = list1

#     def print(self):
#         print('now')

#     def __iter__(self):
#         return Iterator(self)
    
   
        

# class FoodByWeight(Food):
#     def __init__(self, name, price, weight) -> None:
#         self.weight = weight
#         super().__init__(name, price)

#     def weigh_in(self, price_kilo):
#         self.price = self.weight * price_kilo
#         return self.price
    

# class Vegetables(FoodByWeight):
#     def __init__(self, name, price, weight, rot = 0) -> None:
#         self.rot = rot
#         self.list_of_veggies = ['tomato', 'potato', 'onion']
#         super().__init__(name, price, weight)

#     def spoil(self, days, temperature):
#         self.rot = days * (temperature * 1)
#         return self.rot

#     def __str__(self):
#         return str(self.name)
    
#     def add(self):
#         self.list_of_veggies.append(self.name)

# class Meat(FoodByWeight):
#     def __init__(self, name, price, weight, type) -> None:
#         self.type = type
#         self.list_of_meat = []
#         super().__init__(name, price, weight)
    
#     def add(self):
#         self.list_of_meat.append(self.name)

# veg = Vegetables("cabbage", 12, 2)
# veg.spoil(2, 16)
# veg.add()
# iteration = Iterator(veg.list_of_veggies)
# # print(str(veg.name))
# # for n in veg.list_of_veggies:
# #     print(n)

# bolony = Meat('bolony', 2, 3, 'kolbasa')
# bolony.add()
# for i in bolony.list_of_meat:
#     print(i)


      

# class Recteangle:
#     def __init__(self, length, width) -> None:
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width
    
#     def calculate_perimeter(self):
#         return self.length * 2 + self.width * 2
    

# class Square(Recteangle):
#     def __init__(self, length) -> None:
#         super().__init__(length, length)


# class Cube(Square):
#     def calculate_surface_area(self):
#         surface_area = super().calculate_area()
#         return surface_area * 6       
    
#     def volume(self):
#         surface_area = super().calculate_area()
#         surface_area * self.length





# class NumbersIterator:
#     def __init__(self, numbers_instance: 'Numbers') -> None:
#         self.numbers_to_iterate = numbers_instance
#         self.position = - 1

#     def __next__(self) -> int:
#         self.position += 1
#         if self.position < len(self.numbers_to_iterate):
#             return self.numbers_to_iterate[self.position]
#         else:
#             raise StopIteration

    
# class Numbers:
#     def __init__(self) -> None:
#         self._data = [1, 2, 3, 4]
    
#     def __getitem__(self, index: int):
#         return self._data[index]
    
#     def __setitem__(self, index: int, value):
#         self._data[index] = value

#     def __iter__(self):
#         print('inside iter')
#         return NumbersIterator(self)

#     def __contains__(self, value):
#         print('inside contains')
#         return value in self._data
    
#     def __len__(self):
#         return len(self._data)
    
#     def __str__(self) -> str:
#         return str(self._data)
    
#     def __repr__(self) -> str:
#         # От representation - показать "техническое" строковое представление для программиста
#         return f'Object Numbers with {self._data}'







# class Iterator:
#     def __init__(self, item_to_iterate) -> None:
#         self.item_to_iterate = item_to_iterate
#         self.position = - 1

#     def __next__(self):
#         self.position += 1
#         if self.position < len(self.item_to_iterate):
#             return self.item_to_iterate[self.position]
#         else:
#             raise StopIteration


# class Mammal:
#     def __init__(self, color, legs_count = 4) -> None:
#         self.color = color
#         self.legs_count = legs_count

#     def make_sound(self):
#         return f'unknown sound'
    
#     def __str__(self):
#         return str(self.color)
    
#     def __len__(self):
#         return len(self.legs_count)
    

# class Cat(Mammal):
#     def __init__(self, name, color, legs_count = 4) -> None:
#         super().__init__(color, legs_count)
#         self.name  = name
        
#     def make_sound(self):
#         return f'Meow'

#     def __str__(self):
#         return str(self.name)

#     def __contains__(self, value):
#         return value in self.color
    
#     def __iter__(self):
#         return Iterator(self)
    









# class SportMatchInfo:
#     def __init__(self) -> None:
#         self.score = {'home team': 0, 'guest team': 0, 'score': [0, 0]}

#     def __getitem__(self, key):
#         return self.score[key]
    
#     def __setitem__(self, key):
#         if key == 'guest team':
#             self.score[key] += 1
#             self.score['score'][1] += 1

#         elif key == 'home team':
#             self.score[key] += 1
#             self.score['score'][0] += 1

#     def get_score(self):
#         return self.__getitem__('score')
    
#     def team_scores(self, team):
#         self.__setitem__(team)

# game = SportMatchInfo()




# class Iterator:
#     def __init__(self, item) -> None:
#         self.item = item
#         self.position = - 1

#     def __next__(self):
#         self.position += 1
#         if self.position < len(self.item):
#             return self.item[self.position]
#         else:
#             raise StopIteration

# class InTheBox:
#     def __init__(self, name) -> None:
#         self.container = {'name': name, 'item count': 0, 'items': []}

#     def __getitem__(self, key):
#         return self.container[key]
        
#     def __setitem__(self, new_item):
#         self.container['items'].append(new_item)
#         self.container['item count'] += 1

#     def show_items(self):
#         return self.__getitem__('items')
    
#     def show_item_count(self):
#         return self.__getitem__('item count')
    
#     def add_item(self, item):
#           self.__setitem__(item)

#     def __iter__(self):
#         return Iterator(self)

# boxxx = InTheBox('box')






# class BankRecord:
#     def __init__(self, name) -> None:
#         self.record = {'name': name, 'balance': 100, 'transaction': [100]}

#     def __getitem__(self, key):
#         return self.record[key]
    
#     def __setitem__(self, key, newvalue):
#         if key == 'balance' and newvalue != None:
#             self.record[key] += newvalue
        
#         elif key == 'transaction' and newvalue != None:
#             self.record[key].append(newvalue)

#     def getBalance(self):
#         return self.__getitem__('balance')
    
#     def updateBalance(self, new_transaction):
#         self.__setitem__('balance', new_transaction)
#         self.__setitem__('transaction', new_transaction)

#     def getTransaction(self):
#         return self.__getitem__('transaction')
    
#     def numTransactions(self):
#         return len(self.record['transaction'])
    
# joe = BankRecord('Joe')







# class Iterator:
#     def __init__(self, item_to_iterate: 'TableContents'):
#         self.item_to_iterate = item_to_iterate
#         self.position = - 1

#     def __next__(self):
#         self.position += 1
#         if self.position < len(self.item_to_iterate):
#             return self.item_to_iterate[self.position]
#         else:
#             raise StopIteration


# class TableContents:
#     def __init__(self, name, color) -> None:
#         self.name = name
#         self.color = color
#         self.contents = ['phone', 'knife', 'perfume', 'PS4']

#     def __iter__(self):
#         return Iterator(self)
    
#     def __getitem__(self, index):
#         return self.contents[index]
    
#     def __setitem__(self, item):
#         self.contents.append(item)

#     def __len__(self):
#         return len(self.contents)
    
#     def __str__(self):
#         return str(self.contents)
    
#     def __repr__(self) -> str:
#         return f'the contents are {self.contents}'
    
#     def __contains__(self, value):
#         return value in self.contents
    

# class BoxOnTheTable(TableContents):
#     def __init__(self, name, color) -> None:
#         super().__init__(name, color)
#         self.box_contents = []

#     def __setitem__(self, item):
#         self.box_contents.append(item)

#     def add_from_the_table(self, item):
#         if item in self.contents:
#             self.__setitem__(item)

#     def __repr__(self) -> str:
#         return f'the contents are {self.box_contents}'
    
    
# table = TableContents('table', 'black')

# box = BoxOnTheTable('box', 'brown')


# class Container:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y

#     def __setitem__(self, key, value):
#         self.items[key] = value

#     def __getitem__(self, key):
#         return self.items[key]
    
#     def __str__(self):
#         return f'{self.x}, {self.y}'
    
#     # def __repr__(self) -> str:
#     #     return f'{self.items}'
    
#     def __add__(self, other):
#         sum_x = self.x + other.x
#         sum_y = self.y + other.y
#         return Container(sum_x, sum_y)
    
#     def __mul__(self, number):
#         return self.x * number, self.y * number
    
#     def __rmul__(self, number):
#         return self * number
    
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
    



def fun():
    a = input('text: ')
    b = input('text: ')
    c = input('text: ')
    return (a, b, c)

let_a, let_b, let_c = fun()
print(let_a, let_b, let_c)
    









