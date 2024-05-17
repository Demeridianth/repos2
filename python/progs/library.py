import collections


"""library program"""


Record = collections.namedtuple('Record', ['book_type', 'title', 'autor'])


class LibraryRecords:
    def __init__(self) -> None:
        self.records = []

    def add_record(self, new_record):
        self.records.append(new_record)

    def __getitem__(self, record):
        return self.records[record]
    
    

# match/case implemantation

book = Record('Book', 'War and Peace', 'Tolstoy')

