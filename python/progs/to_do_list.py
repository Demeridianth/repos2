import json
def help(to_do):
    print('help text')

def add_task(to_do_tasks):
    add_task = get_user_input('enter task name: ')
    task_new = {'name': add_task, 'status': 'new'}
    to_do_tasks.append(task_new)

def list_tasks(to_do_tasks):
    for index, task in enumerate(to_do_tasks, start=1):
        task_name = task['name']
        task_status = task['status']
        print(f'{index}. {task_name}; {task_status}')

def delete_task(to_do_tasks):
    item_to_remove = get_user_input('select the number of the task to delete it: ', int)
    if 1 <= item_to_remove <= len(to_do_tasks):
        to_do_tasks.pop(item_to_remove - 1)

def replace_task_name(to_do_tasks):
    which_task = int(input('choose the number of the task: '))
    new_name = input('choose a new task name: ')
    to_do_tasks[which_task - 1]['name'] = new_name

def replace_task_status(to_do_tasks):
    which_task = int(input('choose the number of the task: '))
    new_status = input('choose a new status name: ')
    to_do_tasks[which_task - 1]['status'] = new_status


def save_to_disk(name):
    name =  input('give your file a name: ')
    write_to_json(name)

def write_to_json(name):
    with open(f'{name}.json', 'w') as write_to_drive:
        generated_json = json.dumps(tasks)
        write_to_drive.write(generated_json)
        write_to_drive.close()


def read_from_disk(read):
    read = input('select a file to read from: ')
    read_from_json(read)

def read_from_json(read):
    with open(read, 'r') as read_from_drive:
        read_list =  read_from_drive.read()
        read_json = json.loads(read_list)
        read_from_drive.close()
        print(read_json)


def get_user_input(message, converter=str):
    user_input = converter(input(message))
    return user_input

# tasks = []
# while True:
#     choose = input('choose an action: ')
#     if choose == 'help':
#         help()
#     elif choose == 'exit' or choose == 'quit':
#         break
#     elif choose == 'add':
#         add_task(tasks)
#     elif choose == 'list':
#         list_tasks(tasks)
#     elif choose == 'delete':
#         delete_task(tasks)
#     elif choose == 'replace name':
#         replace_task_name(tasks)
#     elif choose == 'replace status':
#         replace_task_status(tasks)
#     elif choose == 'write':
#         write_to_json(tasks)
#     elif choose == 'read':
#         read_from_json(tasks)
#     else:
#         print('unknown command, choose a command')
        
commands = {
    'help': help,
    'exit': quit,
    'quit': exit,
    'add': add_task,
    'list': list_tasks,
    'delete': delete_task,
    'replace name': replace_task_name,
    'replace status': replace_task_status,
    'read': read_from_disk,
    'save': save_to_disk
}

tasks = []
while True:
    choose = input('choose an action: ')
    if choose in commands:
        commands[choose](tasks) 
    else:
        print('unknown command, choose a command')
