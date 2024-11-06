from typing import NamedTuple
import json
import os
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import locale
import numpy as np


"""library database"""

# class separation
# match/case implemantation
# try/except usage
# auto ID implementation for each record
# implementation of different python libraries and modules
# web sraping



Record = NamedTuple('Record', id_number=int, genre=str, title=str, author=str, date_time=str)


class InMemoryLibraryRecords:
    def __init__(self) -> None:
        self.records = []

    def get_records(self) -> list:
        return self.records

    def __getitem__(self, index: int) -> dict:
        return self.records[index]
    

class InJsonFileLibraryRecords:
    def __init__(self, records) -> None:
        self.records = records

    def write_to_json_file(self, records: list) -> None:
        with open(self.records, 'w') as file:
            file.write(json.dumps(records))

    def read_from_json_file(self) -> list:
        if not os.path.exists(self.records):
            self.write_to_json_file([])
        with open(self.records, 'r') as file:
            return json.loads(file.read())

        
class ConsoleUI:
    @staticmethod
    def get_user_input(message: str, converter: type = str) -> str:
        return converter(input(message))
    
    @staticmethod
    def get_record_data() -> tuple:
        genre = ConsoleUI.get_user_input('enter genre for the record: ')
        title = ConsoleUI.get_user_input('enter title for the record: ')
        author = ConsoleUI.get_user_input('enter author for the record: ')
        return (genre, title, author)

    @staticmethod
    def convert_to_dict(record: Record) -> dict:
        return record._asdict()

    @staticmethod
    def list_all_records(records: list) -> None:
    # Print the column headers
        print(f'{"Title":30} {"Author":20} {"Genre":15} {"ID Number":10} {"Date and Time"}')
        print('-' * 90)  
    # Print each record
        for record in sorted(records, key=lambda x: x['author']):
            print(f'{record["title"]:30} {record["author"]:20} {record["genre"]:15} {record["id_number"]:<10} {record["date_time"]}')

    # pattern matching | search library record by author name
    @staticmethod
    def search_library(records: list, author_name: str) -> None:
        for record in records:
            match record:
                case {'author': author, 'title': title, **details} if author == author_name:
                    print(f'{title} | {details}')

    # auto ID implementation for each record
    @staticmethod
    def parse_max_id_number(records: list) -> int:
        id_numbers =  [record['id_number'] for record in records]
        if not id_numbers:
            id_numbers.append(0)
        return max(id_numbers) + 1
    
    # read from text file using pathlib module
    @staticmethod
    def read_text_file(file: str) -> None:
        if not os.path.exists(file):
            with open(file, 'w') as text_file:
                text_file.write(ConsoleUI._scrape_text())
        path = Path.cwd() / file
        print(path.read_text())

    # web scraping text using BeautifulSoup | requests 
    @staticmethod
    def _scrape_text() -> str:
        url = 'https://en.wikipedia.org/wiki/Web_scraping'
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f" _scrape_text method failed to retrieve page with status code {response.status_code}")
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        return paragraphs[1].get_text()
    
    @staticmethod
    def get_datetime() -> str:
        user_locale = locale.getlocale()
        try:
            locale.setlocale(locale.LC_TIME, user_locale)
        except locale.Error:
            print(f'Locale {user_locale} is not supported on your system. Falling back to "C" locale')
            locale.setlocale(locale.LC_TIME, 'C')
        today = datetime.now()
        return f'{today:%c}'


# business logic
def main():
    console = ConsoleUI()
    json_file = InJsonFileLibraryRecords('library.json')
    records_data = InMemoryLibraryRecords()

    # fill InMemoryLibraryRecords with data from JSON file while it is empty:
    try:
        data = json_file.read_from_json_file()
        for record in data:
            records_data.records.append(record)
    except json.decoder.JSONDecodeError:            
        pass


    while True:
        chosen_action = console.get_user_input('\nchoose a command: ')

        if chosen_action == 'list':
            console.list_all_records(records_data.records)

        elif chosen_action == 'add':
            date_time = console.get_datetime()
            id_number = console.parse_max_id_number(records_data.records)
            genre, title, author = ConsoleUI.get_record_data()
            converted_record = ConsoleUI.convert_to_dict(Record(id_number=int(id_number), genre=genre, title=title, author=author, date_time=date_time))
            records_data.records.append(converted_record)
            json_file.write_to_json_file(records_data.records)

        elif chosen_action == 'edit':
            records = records_data.get_records()
            chosen_record = int(input('choose record id number: '))
            for record in records:
                if chosen_record == record['id_number']:
                    print('update record:')
                    genre, title, author = console.get_record_data()
                    record['genre'] = genre; record['title'] = title; record['author'] = author
            json_file.write_to_json_file(records_data.records)

        elif chosen_action == 'delete':
            records = records_data.get_records()
            chosen_record = console.get_user_input('choose record id number: ', int)
            for record in records:
                if chosen_record == record['id_number']:
                    records.remove(record)
            json_file.write_to_json_file(records_data.records)
 
        elif chosen_action == 'search':
            records = records_data.get_records()
            author_name = console.get_user_input('enter author name: ')
            console.search_library(records, author_name)

        elif chosen_action == 'about':
            console.read_text_file('about.txt')

        elif chosen_action == 'quit' or chosen_action == 'q':
            break

        elif chosen_action == 'help':
            print('-------')
            print(' list = view all library records\n', 
                  'add = add a record\n',
                  'edit = edit a record\n',
                  'delete = delete a record\n',
                  'serch = search the library for a record\n',
                  'about = see info about library\n',
                  'quit, q = exit library_data')
            print('-------')

        else:
            print("unknown command, type help for a list of available commands")


if __name__ == '__main__':
    main()
    









    
    
    
    





