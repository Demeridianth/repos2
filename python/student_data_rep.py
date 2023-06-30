import json
import os


class Student:
    def __init__(self, name: str, birthday: str, credit_points: int) -> None:
        self.name = name
        self.birthday = birthday
        self.credit_points = credit_points

    def __repr__(self):
        return f'{self.name}, {self.birthday}, {self.credit_points}'
    
    def convert_to_dict(self) -> dict:
        return {'name': self.name, 'birthday': self.birthday, 'credit points': self.credit_points}



class InMemoryStudentsData:
    def __init__(self) -> None:
        self.students = []

    def get_all_students(self) -> list:
        return self.students
    
    def add_student(self, new_student) -> None:
        self.students.append(new_student)

    def __repr__(self) -> str:
        return f'{self.students}'

    
class ConsoleUI:

    @staticmethod
    def _get_student_data() -> tuple:
        name = ConsoleUI._get_user_input('enter students name: ')
        birthday = ConsoleUI._get_user_input('enter students birthday: ')
        credit_points = ConsoleUI._get_user_input('enter students credit score: ', int)
        return (name, birthday, credit_points)

    @staticmethod
    def _get_action():
        return ConsoleUI._get_user_input('choose a command: ')

    @staticmethod
    def _list_students(students) -> None:
       for index, student in enumerate(students, start=1):
           name = student['name']
           birthday = student['birthday']
           credit_points = student['credit points']
           print(f'{index}. {name}, {birthday}, {credit_points}')

    @staticmethod
    def _get_user_input(message, converter=str) -> str:
        return converter(input(message))


class JsonFileRepository:
    def __init__(self, filename) -> None:
        self.filename = filename

    def write_to_json_file(self, student_records):
        with open(self.filename, 'w') as students_data:
            students_data.write(json.dumps(student_records))

    def read_from_json_file(self):
        if not os.path.exists(self.filename):
            self.write_to_json_file([])
        try:
            with open(self.filename, 'r') as students_data:
                data = students_data.read()
                loaded_data = json.loads(data)
                return loaded_data
        except json.decoder.JSONDecodeError:
            self.write_to_json_file([])


if __name__ == '__main__':
    ui_functions = ConsoleUI()
    students_data = InMemoryStudentsData()
    students_repository = JsonFileRepository('student_data.json')

    all_students = students_repository.read_from_json_file()
    try:
        for student in all_students:
            students_data.students.append(student)
    except TypeError:
        pass

    while True:
       
        selected_action =  ui_functions._get_action()
        if selected_action == 'add':
            name, birthday, credit_points =  ui_functions._get_student_data()
            new_student = Student(name=name, birthday=birthday, credit_points=credit_points)
            student = new_student.convert_to_dict()
            students_data.add_student(student)
            students_repository.write_to_json_file(students_data.get_all_students())
        elif selected_action == 'list':
            students = students_data.get_all_students()
            ui_functions._list_students(students)
        elif selected_action =='delete':
            students = students_data.get_all_students()
            
        elif selected_action == 'edit':
            ...
        elif selected_action == 'delete':
            ...
        elif selected_action == 'help':
            ...
        elif selected_action == 'q':
            break
        else:
            print('unknown command')
            
           

    

