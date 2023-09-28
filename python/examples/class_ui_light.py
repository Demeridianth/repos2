import json
import os
from typing import Callable


class Student:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self) -> str:
        return f'{self.first_name} {self.last_name} ({self.age})'


class InMemoryStudentsRepository:
    def __init__(self) -> None:
        self.students = []

    def get_all_students(self) -> list[Student]:
        return self.students

    def add_student(self, student: Student) -> None:
        self.students.append(student)


class JsonFileStudentsRepository:
    """
    Репозиторий для хранения данных о студентах в JSON-файлах следующего формата:
    [
        {"first_name" <first_name>, "last_name": <last_name>, "age": <age>},
        ...
    ]
    """
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def get_all_students(self) -> list[Student]:
        student_records = self._read_records_from_file()
        students = self._parse_students_from_records(student_records)
        return students

    def add_student(self, student: Student) -> None:
        student_records = self._read_records_from_file()
        new_student_record = self._convert_student_to_dict(student)
        student_records.append(new_student_record)
        self._write_student_records_to_file(student_records)

    def _write_student_records_to_file(self, student_records: list[dict]) -> None:
        """Записать на диск набор записей (словарей нужного формата)."""
        with open(self.filename, 'w') as data_file:
            data_file.write(json.dumps(student_records))

    def _read_records_from_file(self) -> list[dict]:
        """Прочесть с диска набор записей (словарей нужного формата)."""
        # Если файла еще нет, надо его создать и сохранить в него пустой список студентов
        if not os.path.exists(self.filename):
            self._write_student_records_to_file([])

        # А теперь, когда он точно существует, можно просто его смело читать
        with open(self.filename, 'r+') as data_file:
            data = data_file.read()

        return json.loads(data)

    def _parse_students_from_records(self, student_records: list[dict]) -> list[Student]:
        """Сконвертировать набор записей (словарей нужного формата) в набор объектов Student."""
        result = []
        for record in student_records:
            student = Student(first_name=record['first_name'], last_name=record['last_name'], age=record['age'])
            result.append(student)
        return result

    def _convert_student_to_dict(self, student: Student) -> dict:
        """Сконвертировать объект Student в словарь подходящего для записи в файл формата."""
        return {
            'first_name': student.first_name,
            'last_name': student.last_name,
            'age': student.age,
        }


class ConsoleUI:
    @staticmethod
    def list_available_actions() -> None:
        print('add, list, help, quit')

    @staticmethod
    def get_student_data() -> tuple[str, str, int]:
        first_name = ConsoleUI.get_user_input('Введите имя студента: ')
        last_name = ConsoleUI.get_user_input('Введите фамилию студента: ')
        age = ConsoleUI.get_user_input('Введите возраст студента: ', converter_func=int)
        return first_name, last_name, age

    @staticmethod
    def list_students(students: list[Student]) -> None:
        print(students)

    @staticmethod
    def get_action() -> str:
        return ConsoleUI.get_user_input('Введите желаемое действие: ')

    @staticmethod
    def get_user_input(prompt_text: str, converter_func: Callable = str):
        user_input = input(prompt_text)
        return converter_func(user_input)


if __name__ == '__main__':
    # Репозиторий нужен для взаимодействия с хранилищем данных
    students_repository = JsonFileStudentsRepository(filename='students.json')
    ui_functions = ConsoleUI

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
            new_student = Student(first_name=first_name, last_name=last_name, age=age)
            students_repository.add_student(new_student)
        elif selected_action == 'quit':
            break