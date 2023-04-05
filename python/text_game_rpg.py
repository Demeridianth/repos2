# while True:
#     print('Type q to quit\n')
#     answer = input('Guess a number between 1 and 10\n')
    
#     if answer == 'q':
#         break
#     if answer == '5':
#         print('!!!you are correct!!!')
#         break
#     print('!!!you are wrong, try again!!!')


choices = ['Get up', 'Lay around some more', 'Look Around']
while True:
    story = print('You wake up with a headache trying to think of the next action:')
    for index, choice in enumerate(choices, start=1):
        print(f'{index}. {choice}')
    answer = input('\n')
    if answer == '1':
        break

print('next')

choices1 = ['Stand and think', 'GO']
while True:
    story = print('Go to the kitchen?')
    for index, choice in enumerate(choices1, start=1):
        print(f'{index}. {choice}')
    answer = input('\n')
    if answer == '2':
        break


    

        
