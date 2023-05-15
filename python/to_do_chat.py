def help_func():
    print('help text')

def add_task(to_do_tasks):
    add_task = get_user_input('enter task name: ')
    task_new = {'name': add_task, 'status': 'new'}
    to_do_tasks.append(task_new)

def list_tasks():
    for index, task in enumerate(tasks, start=1):
        task_name = task['name']
        task_status = task['status']
        print(f'{index}. {task_name} [{task_status}]')

def delete_task():
    item_to_remove = int(input('select the number of the task to delete it: '))
    if item_to_remove - 1 in range(len(tasks)):
        tasks.pop(item_to_remove - 1)

def get_user_input(message, converter=str):
    user_input = converter(input(message))
    return user_input

# map commands to functions
commands = {
    'help': help_func,
    'exit': exit,
    'quit': exit,
    'add': add_task,
    'list': list_tasks,
    'delete': delete_task
}

tasks = []
while True:
    choose = input('choose an action: ')
    if choose in commands:
        commands[choose](tasks) # call the mapped function with the tasks list
    else:
        print('unknown command, choose a command')