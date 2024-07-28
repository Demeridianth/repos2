#1

# questions = ["What is your name?", "What is your favorite color?", "What is your quest?"]
# n = 0
# while True:
#     print("Type q to quit")
#     answer = input(questions[n])
#     if answer == "q":
#         break
#     n = (n + 1) % 3
    
#     # n += 1
#     # if n > 2:
#     #    n = 0

# print(n)




#2

questions = ['What is your name?', 'What is your favorite color?', 'What is your quest?']
n = 0
while True:
    print('Type q to quit')
    answer = input(questions[n])
    if answer == 'q':
        break
    n += 1
    if n > 2:
        n = 0
