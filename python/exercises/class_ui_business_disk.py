import json
import os

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

    def _write_student_records_to_file(self, student_records):
        """Записать на диск набор записей (словарей нужного формата)."""
        with open(self.filename, 'w') as data_file:
            data_file.write(json.dumps(student_records))

    def _read_records_from_file(self):
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

    def _parse_student_records_from_file(self, student_records):
        """Сконвертировать набор записей (словарей нужного формата) в набор объектов Student."""
        result = []
        for record in student_records:
            student = Student(name=record['name'], last_name=record['last_name'], age=record['age'])
            result.append(record)
        return result
        
    def _conver_student_to_dict(self, student: Student) -> dict:
        """Сконвертировать объект Student в словарь подходящего для записи в файл формата."""
        return {
            'name': student.name,
            'last_name': student.last_name,
            'age': student.age
        }
    
    
class RussianConsoleUI:

    @staticmethod
    def get_action():
        return RussianConsoleUI._get_user_input('enter a command: ')
    
    @staticmethod
    def get_student_data() -> tuple:
        first_name = RussianConsoleUI._get_user_input('Введите имя студнта: ')
        last_name = RussianConsoleUI._get_user_input('Введите фамилию студента: ')
        age = RussianConsoleUI._get_user_input('Введите возраст студента: ', converter_func=int)
        return (first_name, last_name, age)

    @staticmethod
    def list_students(students) -> None:
        for index, student in enumerate(students, start=1):
           name = student['name']
           last_name = student['last_name']
           age = student['age']
           print(f'{index}. {name}, {last_name}, {age}')

    @staticmethod
    def _get_user_input(prompt_text: str, converter_func = str):
        user_input = input(prompt_text)
        return converter_func(user_input)
    
    @staticmethod
    def list_available_actions():
        print('add', 'list', 'delete', 'quit')

# class BusinessLogic:
#     def __init__(self, repository_instance) -> None:
#         self.repository = repository_instance

#     def list_students(self) -> list[Student]:
#         return self.repository.get_all_students()

#     def add_student(self, student: Student) -> None:
#         self.repository.add_student(student)


if __name__ == '__main__':
     # Репозиторий нужен для взаимодействия с хранилищем данных
    students_repository = JsonFileStudentsRepository(filename='students.json')
    ui_functions = RussianConsoleUI
    # business_logic = BusinessLogic(students_repository)

    ui_functions.list_available_actions()
    while True:
        
        selected_action = ui_functions.get_action()
        

        if selected_action == 'help':
            ui_functions.list_available_actions()
        elif selected_action == 'list':
            students = students_repository.get_all_students()
            ui_functions.list_students(students)
        elif selected_action == 'add':
            first_name, last_name, age = ui_functions.get_student_data()
            new_student = Student(first_name, last_name=last_name, age=age)
            students_repository.add_student(new_student)
        elif selected_action == 'quit':
            break