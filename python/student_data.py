import json
import os


class Student:
    def __init__(self, name: str, birthday: str, credit_points: int) -> None:
        self.name = name
        self.birthday = birthday
        self.credit_points = credit_points

    def __repr__(self):
        return f'{self.name}, {self.birthday}, {self.credit_points}'
    
  
    

class Data:
    def __init__(self) -> None:
        self.data = []

    def add_data(self):
        name = self._get_user_input('enter student name: ')
        birthday = self._get_user_input('enter students birthday: ')
        credit_points = self._get_user_input('enter students credit score: ', int)
        student_info = Student(name, birthday, credit_points)
        student_data = student_info.convert_to_dict()
        self.data.append(student_data)
        self.save_to_disk()

    def delete_data(self):
        delete_data = self._get_user_input('choose students number: ', int)
        self.data.pop(delete_data - 1)
        self.save_to_disk()

    def display_student_data(self):
        for index, data in enumerate(self.data, start=1):
            name = data['name']
            birthday = data['birthday']
            credit_points = data['credit points']
            print(f'{index}. {name}; {birthday}, {credit_points}')

    def edit_student_data(self):
        data_number = self._get_user_input('choose students number: ', int)
        data_type = self._get_user_input('choose what data would you like to change: ')
        if data_type == 'name':
            new_name = self._get_user_input('choose a new name: ')
            self.data[data_number - 1]['name'] = new_name
        elif data_type == 'birthday':
            new_birthady = self._get_user_input('choose a new birthday: ')
            self.data[data_number - 1]['birthday'] = new_birthady
        elif data_type == 'credit points':
            new_credit_points = self._get_user_input('update credit points: ', int)
            self.data[data_number - 1]['credit points'] = new_credit_points
        self.save_to_disk()

    def save_to_disk(self):
        with open('student_data.json', 'w') as write_to_drive:
            generated_json = json.dumps(self.data)
            write_to_drive.write(generated_json)
            
    def read_from_disk(self):
        with open('student_data.json', 'r') as read_from_drive:
            read_data = read_from_drive.read()
            read_json = json.loads(read_data)
            for d in read_json:
                self.data.append(d)

    def get_help(self):
        print("list of commands:\n 'add' - add new student's data\n display - display all students data\n change - edit students data\n delete - delete a spicific student's data\n q - leave the programm\n help - display all commands")
            
    def _get_user_input(self, message, converter=str):
        user_input = converter(input(message))
        return user_input
    
    def __repr__(self):
        return f'{self.data}'
    
 

    def choose_command(self):
        
        while True:
            user_input = self._get_user_input('choose a command: ')
            if user_input == 'add':
                self.add_data()
            elif user_input == 'display':
                self.display_student_data()
            elif user_input == 'edit':
                self.edit_student_data()
            elif user_input == 'delete':
                self.delete_data()
            elif user_input == 'help':
                self.get_help()
            elif user_input == 'q':
                break
            else:
                print('unknown command')

class DataIterator:
    def __init__(self, data_instance) -> None:
        self.data_instance = data_instance
        self.position = - 1

    def __next__(self):
        self.position += 1
        if self.position < len(self.data_instance):
            return self.data_instance[self.position]
        else:
            raise StopIteration


data = Data()
data.read_from_disk()
data.choose_command()
