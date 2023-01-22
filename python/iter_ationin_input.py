i = 0
while True:
    print(f'iter No{i} began')
    user_choice = input('stop iter? (y/n): ')
    
    if user_choice == 'y':
        print('user decided to stop current iteration')
        continue

    i += 1
    print(f'iteration No{i} stopped')
