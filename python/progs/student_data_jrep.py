import json
import os


class Student:
    def __init__(self, name: str, birthday: str, credit_points: str) -> None:
        self.name = name
        self.birthday = birthday
        self.credit_points = credit_points

    def __repr__(self) -> str:
        return f'{self.name}, {self.birthday}, {self.credit_points}'   
        

class JsonStudentFileRepository:
    def __init__(self, filename) -> None:
        self.filename = filename

    def add_student(self, student: Student) -> None:
        students_data = self._read_student_records_from_file()
        new_student_data = self._convert_student_to_dict(student)
        students_data.append(new_student_data)
        self._write_student_record_to_file(students_data)

    def get_all_students(self):
        student_data = self._read_student_records_from_file()
        students = self._parse_student_records(student_data)
        return students

    def delete_student(self, number):
        students = self.get_all_students()
        students.pop(number - 1)
        self._write_student_record_to_file(students)

    def edit_data(self, students_number, data_type, new_data):
        students_data = self.get_all_students()
        students_data[students_number - 1][data_type] = new_data
        self._write_student_record_to_file(students_data)

    def _write_student_record_to_file(self, student_records):
        with open(self.filename, 'w') as file_data:
            file_data.write(json.dumps(student_records))

    def _read_student_records_from_file(self):
        if not os.path.exists(self.filename):\
            self._write_student_record_to_file([])
        with open(self.filename, 'r') as file_data:
            data = file_data.read()
            return json.loads(data)
        
    def _convert_student_to_dict(self, student: Student) -> dict:
        return {
            'name': student.name,
            'birthday': student.birthday,
            'credit points': student.credit_points
        }
    
    def _parse_student_records(self, students_records):
        result = []
        for record in students_records:
            result.append(record)
        return result
    

class ConsoleUI:

    @staticmethod
    def _get_student_data() -> tuple:
        name = ConsoleUI._get_user_input('enter students name: ')
        birthday = ConsoleUI._get_user_input('enter students birthday: ')
        credit_points = ConsoleUI._get_user_input('enter students credit points: ')
        return (name, birthday, credit_points)
    
    @staticmethod
    def _list_students(students):
        for index, student in enumerate(students, start=1):
           name = student['name']
           birthday = student['birthday']
           credit_points = student['credit points']
           print(f'{index}. {name}, {birthday}, {credit_points}')

    @staticmethod
    def _get_action():
        return ConsoleUI._get_user_input('choose a command: ')

    @staticmethod
    def _get_user_input(message, converter=str) -> str:
        return converter(input(message))
    
    @staticmethod
    def _get_students_number() -> int:
        return ConsoleUI._get_user_input('enter students number: ', int)
    
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



if __name__ == '__main__':
    
    students_repository = JsonStudentFileRepository('student_data.json')
    ui_functions = ConsoleUI()

    while True:
        selected_action =  ui_functions._get_action()

        if selected_action == 'add':
            name, birthday, credit_points = ui_functions._get_student_data()
            student = Student(name, birthday, credit_points)
            students_repository.add_student(student)

        elif selected_action == 'list':
            students = students_repository.get_all_students()
            ui_functions._list_students(students)

        elif selected_action =='delete':
            students_number = ui_functions._get_students_number()
            students_repository.delete_student(students_number)

        elif selected_action == 'edit':
            students_number = ui_functions._get_students_number()
            data_type = ui_functions._get_data_type()
            new_data = ui_functions._get_new_data()
            students_repository.edit_data(students_number, data_type, new_data)

        elif selected_action == 'help':
            ui_functions.list_all_actions()

        elif selected_action == 'q':
            break
        else:
            print('unknown command')