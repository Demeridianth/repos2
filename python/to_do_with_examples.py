import json
def help():
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

    # task_name = []
    # for index, task in enumerate(tasks, start=1):
    #     for key, value in task.items():
    #         task_name.append(value)
    #         task_to_string = str(task_name)
    #         task_status = task_to_string.replace('[', '').replace(']', '').replace("'", '')
    #     print(f'{index}. {task_status}')

    # for index, task in enumerate(tasks, start=1):
    #     to_string = str(task)
    #     replaced = to_string.replace('{', '').replace('}', '').replace("'", '')
    #     print(f' {index}. {replaced}')

def delete_task(to_do_tasks):
    # item_to_remove = int(input('select the number of the task to delete it: '))
    # for index, task in enumerate(tasks):
    #     if index + 1 == item_to_remove:
    #         del tasks[item_to_remove]

    # item_to_remove = int(input('select the number of the task to delete it: '))
    # if 1 <= item_to_remove <= len(to_do_tasks):
    #     to_do_tasks.pop(item_to_remove - 1)

    item_to_remove = get_user_input('select the number of the task to delete it: ', int)
    if 1 <= item_to_remove <= len(to_do_tasks):
        to_do_tasks.pop(item_to_remove - 1)

    # item_to_remove = int(input('select the number of the task to delete it: '))
    # del tasks[item_to_remove - 1]

    # item_to_delete = input('select an item to delete: ')
    # for z in tasks:
    #     for key, value in z.items():
    #         if value == item_to_delete:

def replace_task_name():
    which_task = int(input('choose the number of the task: '))
    new_name = input('choose a new task name: ')
    tasks[which_task - 1]['name'] = new_name
    
    # for index, task in enumerate(tasks):
        #     if index + 1 == which_task:
        #         task['name'] = new_name

def replace_task_status():
    which_task = int(input('choose the number of the task: '))
    new_status = input('choose a new status name: ')
    tasks[which_task - 1]['status'] = new_status

def write_to_json():
    write_to_drive = open('to_do_list.json', 'w')
    generate_json = json.dumps(tasks)
    write_to_drive.write(generate_json)
    write_to_drive.close()

def read_from_json():
    read_from_drive = open('to_do_list.json', 'r')
    read_list =  read_from_drive.read()
    read_from_drive.close()
    read_json = json.loads(read_list)
    print(read_json)

def get_user_input(message, converter=str):
    user_input = converter(input(message))
    return user_input

tasks = []
while True:
    choose = input('choose an action: ')
    if choose == 'help':
        help()
    elif choose == 'exit' or choose == 'quit':
        break
    elif choose == 'add':
        add_task(tasks)
    elif choose == 'list':
        list_tasks(tasks)
    elif choose == 'delete':
        delete_task(tasks)
    elif choose == 'replace name':
        replace_task_name()
    elif choose == 'replace status':
        replace_task_status()
    elif choose == 'write':
        write_to_json()
    elif choose == 'read':
        read_from_json()
    else:
        print('unknown command, choose a command')
        
    # write_to_drive = open('to_do_list.json', 'w')
    # generate_json = json.dumps(tasks)
    # write_to_drive.write(generate_json)
    # write_to_drive.close()