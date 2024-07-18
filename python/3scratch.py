records = [{'id_number': '3', 'genre': 'novel', 'title': 'War and Peace', 'author': 'Tolstoy'}, {'id_number': '2', 'genre': 'novel', 'title': 'Crime and Punishment', 'author': 'DOstoyevsky'}]

# book = str(input('your book name?: '))
# for record in records:
#     match record:
#         case {'title': book, **details}:
#             print(f'title: {book} | {details}')


records = [{'id_number': '3', 'genre': 'novel', 'title': 'War and Peace', 'author': 'Tolstoy'}, 
           {'id_number': '2', 'genre': 'novel', 'title': 'Crime and Punishment', 'author': 'Dostoyevsky'}]

book = str(input('Your book name?: '))
for record in records:
    match record:
        case {'title': title, **record_details} if title == book:
            print(f"{title} | {record_details}")








    



