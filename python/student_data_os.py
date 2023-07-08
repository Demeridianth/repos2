import json
import os


class Student:
    def __init__(self, name: str, birthday: str, credit_points: str) -> None:
        self.name = name
        self.birthday = birthday
        self.credit_points = credit_points

    def __repr__(self) -> str:
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
        credit_points = ConsoleUI._get_user_input('enter students credit score: ')
        return (name, birthday, credit_points)

    @staticmethod
    def _get_action() -> str:
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
    
    @staticmethod
    def _get_students_number() -> int:
        number = ConsoleUI._get_user_input('enter students number: ', int)
        return number

    @staticmethod
    def _get_data_type() -> str:
        data_type = ConsoleUI._get_user_input('choose what data would you like to change: ')
        return data_type
    
    @staticmethod
    def _get_new_data() -> str:
        new_data = ConsoleUI._get_user_input('enter new data: ')
        return new_data
    
    @staticmethod
    def list_all_actions():
        print(f'"add", "list", "delete", "edit", "help"')



class JsonFileRepositoryActions:
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
    students_repository = JsonFileRepositoryActions('student_data.json')

    all_students = students_repository.read_from_json_file()
    try:
        for student in all_students:
            students_data.add_student(student)
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
            number = ui_functions._get_students_number()
            students.pop(number - 1)
            students_repository.write_to_json_file(students_data.get_all_students())

        elif selected_action == 'edit':
            students = students_data.get_all_students()
            student_number = ui_functions._get_students_number()
            data_type = ui_functions._get_data_type()
            new_data = ui_functions._get_new_data()
            students[student_number - 1][data_type] = new_data
            students_repository.write_to_json_file(students_data.get_all_students())
        elif selected_action == 'help':
                ui_functions.list_all_actions()
        elif selected_action == 'q':
                break
        else:
            print('unknown command')
            
           

    

