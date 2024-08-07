import collections
import json
import os


"""library"""

# match/case implemantation (maybe for 'search' command)  DONE  !!!
# use dict.get() on 'edit' or elsewhere
# maybe use dict.setdefault.append on 'add' or 'edit'
# use os.path or pathlib for something = in command 'about' print a text with info about library
# maybe a download command, requests module
# classes must be separated    DONE !!!
# add book id_number automatic the next number after the largest existing or a random but not existing - ADD !!!   DONE!!
# add date and time - when the record was created  !!!
# annotations to everything

# user/admin access !!!




Record = collections.namedtuple('Record', ['id_number', 'genre', 'title', 'author'])


class InMemoryLibraryRecords:
    def __init__(self):
        self.records = []

    def get_records(self):
        return self.records

    def __getitem__(self, index: int):
        return self.records[index]
    

class InJsonFileLibraryRecords:
    def __init__(self, records):
        self.records = records

    def write_to_json_file(self, records):
        with open(self.records, 'w') as file:
            file.write(json.dumps(records))

    def read_from_json_file(self):
        if not os.path.exists(self.records):
            self.write_to_json_file([])
        with open(self.records, 'r') as file:
            return json.loads(file.read())

    # method not yet needed
    # def parse_library_records_from_file(self, records):
    #     result = [Record(genre=record['genre'], title=record['title'], author=record['author']) for record in records]
    #     return result

        
class ConsoleUI:
    @staticmethod
    def get_user_input(message, converter=str):
        return converter(input(message))
    
    @staticmethod
    def get_record_data():
        genre = ConsoleUI.get_user_input('enter genre for the record: ')
        title = ConsoleUI.get_user_input('enter title for the record: ')
        author = ConsoleUI.get_user_input('enter author for the record: ')
        return (genre, title, author)
    
    # @staticmethod
    # def new_record():
    #     id_number, genre, title, author = ConsoleUI.get_record_data()
    #     return ConsoleUI.convert_to_dict(Record(id_number=id_number, genre=genre, title=title, author=author))
        
    @staticmethod
    def _convert_to_dict(record: Record):
        return {'id_number': record.id_number, 'genre': record.genre, 'title': record.title, 'author': record.author}
    
    @staticmethod
    def list_all_records(records):
        for record in sorted(records, key=lambda x: x['author']):
            print(f'{record["title"]}, {record["author"]}, {record["genre"]}, {record["id_number"]}')

    # pattern matching
    @staticmethod
    def search_library(records, author_name):
        for record in records:
            match record:
                case {'author': author, 'title': title, **details} if author == author_name:
                    print(f'{title} | {details}')

    # for auto ID implementation for each record
    @staticmethod
    def parse_max_id_number(records):
        id_numbers =  [record['id_number'] for record in records]
        if not id_numbers:
            id_numbers.append(0)
        return max(id_numbers) + 1




if __name__ == '__main__':
    console = ConsoleUI()
    json_file = InJsonFileLibraryRecords('library.json')
    records_data = InMemoryLibraryRecords()

    # fill InMemoryLibraryRecords with data from file, while trying to read from empty JSON file:
    try:
        data = json_file.read_from_json_file()
        for record in data:
            records_data.records.append(record)
    except json.decoder.JSONDecodeError:            
        pass



    # business logic
    while True:
        chosen_action = console.get_user_input('\nchoose a command: ')

        if chosen_action == 'list':
            console.list_all_records(records_data.records)

        elif chosen_action == 'add':
            id_number = console.parse_max_id_number(records_data.records)
            genre, title, author = ConsoleUI.get_record_data()
            converted_record = ConsoleUI._convert_to_dict(Record(id_number=int(id_number), genre=genre, title=title, author=author))
            records_data.records.append(converted_record)
            json_file.write_to_json_file(records_data.records)

        elif chosen_action == 'edit':
            records = records_data.get_records()
            chosen_record = console.get_user_input('choose record id number: ')
            for record in records:
                if chosen_record == record['id_number']:
                    print('update record:')
                    id_number, genre, title, author = console.get_record_data()
                    record['id_number'] = id_number; record['genre'] = genre; record['title'] = title; record['author'] = author
            json_file.write_to_json_file(records_data.records)

        elif chosen_action == 'delete':
            records = records_data.get_records()
            chosen_record = int(console.get_user_input('choose record id number: '))
            for record in records:
                if chosen_record == record['id_number']:
                    records.remove(record)
            json_file.write_to_json_file(records_data.records)

        # search library by author 
        elif chosen_action == 'search':
            records = records_data.get_records()
            author_name = console.get_user_input('enter author name: ')
            console.search_library(records, author_name)


        elif chosen_action == 'quit' or 'q':
            break









    
    
    
    





