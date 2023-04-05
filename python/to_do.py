tasks = []
while True:
    
    choose = input('choose an action: ')
    if choose == 'help':
        print('help text')
    elif choose == 'exit' or choose == 'quit':
        break
    elif choose == 'add':
        add_task = input('enter task name: ')
        task_new = {'text': add_task, 'status': 'new'}
        tasks.append(task_new)
    elif choose == 'list':
        for z in tasks:
            for key, value in z.items():
                print(f'{key}: {value}')
    elif choose == 'delete':
        # item_to_remove = input('select the number of the item to remove\n')
        # del tasks[item_to_remove]
        item_to_delete = input('select an item to delete: ')
        for z in tasks:
            for key, value in z.items():
                if value == item_to_delete:
                    tasks.remove(z)
    else:
        print('unknown command, choose a command')
        

