import json
import os


""" Program that simulates a staff access system; 
An admin will be able to manage other users including updating, deleting or creating new users.  A normal user will only be able to view or update their own details."""


class StaffMember:
    def __init__(self, name, password, account_type):
        self.name = name
        self.password = password
        self.account_type = account_type

    def __repr__(self):
        return f'{self.name}, {self.password}, {self.account_type}'
    
    def convert_to_dict(self):
        return {'name': self.name, 'password': self.password, 'account type': self.account_type}


class Staff: 
    def __init__(self):
        self.staff_members = []

    def get_all_members(self):
        return self.staff_members
    

class ConsoleInterface:
    
    @staticmethod
    def get_user_input(message, converter=str):
        return converter(input(message))
    
    @staticmethod
    def get_member_details_admin():
        name = ConsoleInterface.get_user_input('enter staff members name: ')
        password = ConsoleInterface.get_user_input('enter staff members password: ')
        account_type = ConsoleInterface.get_user_input('enter staff members account type: ')
        return (name, password, account_type)
    
    @staticmethod
    def get_member_details_user():
        name = ConsoleInterface.get_user_input('enter staff members name: ')
        password = ConsoleInterface.get_user_input('enter staff members password: ')
        return (name, password)
    
    @staticmethod
    def add_new_member():
        name, password, account_type = console.get_member_details_admin()
        new_member = StaffMember(name = name, password = password, account_type = account_type)
        staff.staff_members.append(StaffMember.convert_to_dict(new_member))

    @staticmethod
    def display_staff(members):
        for member in sorted(members, key=lambda x: x['name']):
            name = member['name']
            password = member['password']
            account_type = member['account type']
            print(f'{name}, {password}, {account_type}')

    @staticmethod
    def display_specific_user_details():
        print(f'{member["name"]}, {member["password"]}')


class JsonRepository:
    def __init__(self, filename):
        self.filename = filename

    def write_to_file(self, staff_data):
        with open(self.filename, 'w') as data:
            data.write(json.dumps(staff_data))

    def read_from_file(self):
        if not os.path.exists(self.filename):
            self.write_to_file([])
        with open(self.filename, 'r') as data:
            loaded_data = json.loads(data.read())
            return loaded_data


if __name__ == '__main__':
    console = ConsoleInterface()
    json_file = JsonRepository('staff_members.json')
    staff = Staff()

# trying to read from the JSON file that is empty
    try:
        all_staff =  json_file.read_from_file()
        for member in all_staff:
            staff.staff_members.append(member)
    except json.decoder.JSONDecodeError:            
        pass
        
 

    while True:
        
        password_check = console.get_user_input('type q to exit or enter password: ')

        # ADMIN
        if password_check == 'admin':
            while True:
                selected_action = console.get_user_input('choose a command: ')

                if selected_action == 'add':
                    console.add_new_member()
                    json_file.write_to_file(staff.get_all_members())

                elif selected_action == 'edit':
                    selected_member = console.get_user_input('enter users name: ')
                    staff_members = staff.get_all_members()
                    for member in staff_members:
                        if selected_member == member['name']:
                            print('enter new user details!\n')
                            name, password, account_type = console.get_member_details_admin()
                            member['name'] = name
                            member['password'] = password
                            member['account type'] = account_type
                    json_file.write_to_file(staff.get_all_members())

                elif selected_action == 'delete':
                    selected_member = console.get_user_input('enter users name: ')
                    staff_members = staff.get_all_members()
                    for member in staff_members:
                        if selected_member == member['name']:
                            staff_members.remove(member)
                    json_file.write_to_file(staff.get_all_members())

                elif selected_action == 'list':
                    staff_members = staff.get_all_members()
                    console.display_staff(staff_members)

                elif selected_action == 'exit':
                    break

                elif selected_action == 'help':
                    print('add = add new member of staff\n'
                          'edit = edit staff members details\n'
                          'delete = delete staff member from database\n'
                          'list = display all staff members details\n'
                          'exit = return to the main console screen')


        # EXIT PROGRAMM
        elif password_check == 'q':
            break


        # USER
        else:
            staff_members =  staff.get_all_members()
            for member in staff_members:
                if password_check in member['password']:
                    while True:
                        selected_action = console.get_user_input('choose a command: ')

                        if selected_action == 'list':
                            console.display_specific_user_details()

                        elif selected_action == 'edit':
                            print('enter new user details!\n')
                            name, password = console.get_member_details_user()
                            member['name'] = name
                            member['password'] = password
                            json_file.write_to_file(staff.get_all_members())

                        elif selected_action == 'help':
                            print('edit = edit you details\n'
                                  'list = display your details\n'
                                  'exit = return to the main console screen')

                        elif selected_action == 'exit':
                            break
            

            


                


            




