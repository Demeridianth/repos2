import csv
# test_file = open('my_test_file.txt', 'w')
# test_file.write('dont worry, this is just a test\n')

# test_file.close()

# test_file = open('my_test_file.txt', 'r')
# print(test_file.read())



# with open('my_test_file.txt', 'w') as my_file:
#     my_file.write('some other text now')

# with open('my_test_file.txt', 'r') as my_file:
#         print(my_file.read())
# my_list = []
# with open('my_test_file.txt', 'r') as my_file:
#     my_list.append(my_file.read())
#     print(my_list)


# with open('my_csvfile.csv', 'w') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter = ',')
#     spamwriter.writerow(['one', 'two', 'three'])
#     spamwriter.writerow(['four', 'five', 'six'])
answers = ['what is your name', 'your age', 'your sex']

for n in answers:
    print('enter your data\n')
    answer = input(f'{n}\n')
    data_to_file = open('data_file.txt', 'a')
    data_to_file.write(f'{answer}\n')
    data_to_file.close()