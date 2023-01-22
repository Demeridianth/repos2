weather_records = [
    {'country': 'Russia', 'city': 'Moscow', 'date': '2022-01-01', 'temperature': -30},
    {'country': 'Russia', 'city': 'Moscow', 'date': '2022-01-02', 'temperature': -23},
    {'country': 'Russia', 'city': 'Moscow', 'date': '2022-01-03', 'temperature': -27},
    {'country': 'Russia', 'city': 'Saint Petersburg', 'date': '2022-01-01', 'temperature': -34},
    {'country': 'Russia', 'city': 'Saint Petersburg', 'date': '2022-01-02', 'temperature': -26},
    {'country': 'Russia', 'city': 'Saint Petersburg', 'date': '2022-01-03', 'temperature': -12},

    {'country': 'Latvia', 'city': 'Riga', 'date': '2022-01-01', 'temperature': -5},
    {'country': 'Latvia', 'city': 'Riga', 'date': '2022-01-02', 'temperature': -9},
    {'country': 'Latvia', 'city': 'Riga', 'date': '2022-01-03', 'temperature': -4},
    {'country': 'Latvia', 'city': 'Daugavpils', 'date': '2022-01-01', 'temperature': -3},
    {'country': 'Latvia', 'city': 'Daugavpils', 'date': '2022-01-02', 'temperature': -8},
    {'country': 'Latvia', 'city': 'Daugavpils', 'date': '2022-01-03', 'temperature': -2},

    {'country': 'Spain', 'city': 'Barcelona', 'date': '2022-01-01', 'temperature': 0},
    {'country': 'Spain', 'city': 'Barcelona', 'date': '2022-01-02', 'temperature': 6},
    {'country': 'Spain', 'city': 'Barcelona', 'date': '2022-01-03', 'temperature': 9},
    {'country': 'Spain', 'city': 'Madird', 'date': '2022-01-01', 'temperature': -2},
    {'country': 'Spain', 'city': 'Madird', 'date': '2022-01-02', 'temperature': 5},
    {'country': 'Spain', 'city': 'Madird', 'date': '2022-01-03', 'temperature': 11},
]



# file = open('file1.py', 'a')
# file.write('Some text on line1\n')
# file.write('Some text on line2\n')
# file.close()

# file = open('file1.py', 'w')
# lines = ['Some text on line1\n', 'Some text on line2\n']
# file.writelines(lines)
# file.close()

# file = open('file1.py', 'a')

# file.seek(0)
# file.close()
 


# file = open('file1.py', 'r')
# file.read()
# file.seek(0)



# test_file = open('test_file1', 'w')
# lines = ['testing info\n', 'next_line_testing\n']
# test_file.writelines(lines)
# test_file.close()

# test_file = open('test_file1', 'a')
# test_file.write('another line')
# test_file.close()

# test_file = open('test_file1', 'r')
# print(test_file.read())
# test_file.seek(0)
# print(test_file.read(8))
# test_file.seek(0)
# print(test_file.readlines())
# test_file.seek(0)
# print(test_file.readline())
# test_file.close()



# Записать в файл
weather_data_file = open('weather_data.txt', 'w')
for record in weather_records:
    country = record['country']
    city = record['city']
    date = record['date']
    temperature = record['temperature']

    line = f'{country}|{city}|{date}|{temperature}\n'

    weather_data_file.write(line)
weather_data_file.close()


# Прочесть из файла
restored_records = []
weather_data_file = open('weather_data.txt', 'r')
for line in weather_data_file.readlines():
    line = line.replace('\n', '')
    fields = line.split('|')
    record = {'country': fields[0], 'city': fields[1], 'date': fields[2], 'temperature': int(fields[3])}
    restored_records.append(record)


weather_data_file.close()
print(restored_records)




        



  
        



  
