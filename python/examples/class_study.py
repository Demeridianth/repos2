import json
import os


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




# class NumbersIterator:
#     def __init__(self, numbers_instance: 'Numbers') -> None:
#         self._numbers_to_iterate = numbers_instance
#         self._position = -1

#     def __next__(self) -> int:
#         self._position += 1
#         if self._position < len(self._numbers_to_iterate):
#             return self._numbers_to_iterate.get(self._position)
#         else:
#             raise StopIteration


# class Numbers:
#     def __init__(self) -> None:
#         self._data = [1, 2, 3, 4]

#     def __getitem__(self, index: int) -> int:
#         return self._data[index]

#     def __setitem__(self, index: int, value: int) -> None:
#         self._data[index] = value

#     def __iter__(self):
#         # Если метода __contains__ нет, то код:
#         # numbers = Numbers()
#         # value in numbers
#         # вызовет __iterator__
#         # и при помощи полученного итератора переберет все значения
#         print('inside __iter__')
#         return NumbersIterator(self)

#     def __contains__(self, value: int) -> bool:
#         # Если метод __contains__ есть, то код:
#         # numbers = Numbers()
#         # value in numbers
#         # вызовет его
#         print('inside __contains__')
#         return value in self._data

#     def __len__(self) -> int:
#         return len(self._data)

#     def __str__(self) -> str:
#         # Показать строковое представление объекта для человека
#         return str(self._data)

#     def __repr__(self) -> str:
#         # От representation - показать "техническое" строковое представление для программиста
#         return f'<Объект Numbers c числами {self._data}>'





# разделение и ответственность!


class Student:
    def __init__(self, name: str, last_name: str, age: int) -> None:
        self.name = name
        self.last_name = last_name
        self.age = age

    def __repr__(self) -> str:
        return f'{self.name}, {self.last_name}, {self.age}'
    
    
    
# class Program:
#     def __init__(self, students=None) -> None:
#         # self.students = []
#         # if students is not None:
#         #     self.students = students
#         if students == None:
#             self.students = []
#         else:
#             self.students = students

#     def list(self) -> list[Student]:
#         return self.students
    
#     def add_student(self, first_name: str, last_name: str, age: int):
#         new_student = Student(first_name=first_name, last_name=last_name, age=age)
#         self.students.append(new_student)


class InMemoryStudentsRepository:
    def __init__(self) -> None:
        self.students = []

    def get_all_students(self):
        return self.students
    
    def add_student(self, student: Student):
        self.students.append(student)


class JsonFileStudentsRepository:
    """
    Репозиторий для хранения данных о студентах в JSON-файлах следующего формата:
    [
        {"first_name" <first_name>, "last_name": <last_name>, "age": <age>},
        ...
    ]
    """
    def __init__(self, filename) -> None:
        self.filename = filename

    def get_all_students(self):
        student_records = self._read_records_from_file()
        students = self._parse_student_records_from_file(student_records)
        return students

    def add_student(self, student: Student):
        student_records = self._read_records_from_file()
        new_student_record = self._conver_student_to_dict(student)
        student_records.append(new_student_record)
        self._write_student_records_to_file(student_records)

    def _write_student_records_to_file(self, student_records: list[dict]) -> None:
        """Записать на диск набор записей (словарей нужного формата)."""
        with open(self.filename, 'w') as data_file:
            data_file.write(json.dumps(student_records))

    def _read_records_from_file(self) -> list[dict]:
        """Прочесть с диска набор записей (словарей нужного формата)."""
        # Если файла еще нет, надо его создать и сохранить в него пустой список студентов"""
        if not os.path.exists(self.filename):
            self._write_student_records_to_file([])

            
        # try:
        #     with open(self.filename, 'r') as data_file:
        #         data = data_file.read()
        # except FileNotFoundError:
        #     self._write_student_records_to_file([])


        # А теперь, когда он точно существует, можно просто его смело читать
        with open(self.filename, 'r') as data_file:
            data = data_file.read()
        return json.loads(data)

    def _parse_student_records_from_file(self, student_records: list[dict]) -> list[Student]:
        """Сконвертировать набор записей (словарей нужного формата) в набор объектов Student."""
        result = []
        for record in student_records:
            student = Student(first_name=record['first_name'], last_name=record['last_name'], age=record['age'])
            result.append(student)
        return result
        
    def _conver_student_to_dict(self, student: Student) -> dict:
        """Сконвертировать объект Student в словарь подходящего для записи в файл формата."""
        return {
            'name': student.name,
            'last_name': student.last_name,
            'age': student.age
        }
    
    
class ConsoleUI:

    @staticmethod
    def get_action():
        return ConsoleUI._get_user_input('enter a command: ')
    
    @staticmethod
    def get_student_data() -> tuple(str, str, int):
        first_name = ConsoleUI._get_user_input('Введите имя студнта: ')
        last_name = ConsoleUI._get_user_input('Введите фамилию студента: ')
        age = ConsoleUI._get_user_input('Введите возраст студента: ', converter_func=int)
        return (first_name, last_name, age)

    @staticmethod
    def list_students(students: list[Student]) -> None:
        print(students)

    @staticmethod
    def _get_user_input(prompt_text: str, converter_func = str):
        user_input = input(prompt_text)
        return converter_func(user_input)
    
    @staticmethod
    def list_available_actions():
        print('add', 'list', 'delete', 'quit')


if __name__ == '__main__':
     # Репозиторий нужен для взаимодействия с хранилищем данных
    student_repository = JsonFileStudentsRepository(filename='students.json')
    ui_functions = ConsoleUI

    ui_functions.list_available_actions()
    while True:
        ui_functions.list_available_actions()
        selected_action = ui_functions.get_action()
        

        if selected_action == 'help':
            ui_functions.list_available_actions()
        elif selected_action == 'list':
            students = student_repository.get_all_students()
            ui_functions.list_students()
        elif selected_action == 'add':
            first_name, last_name, age = ui_functions.get_student_data()
            new_student = Student(first_name=first_name, last_name=last_name, age=age)
            student_repository.add_student(new_student)
        elif selected_action == 'qConsoleUIt':
            break
        


