import json
class Iterator:
    def __init__(self, instance: 'Tasks') -> None:
        self.intstance = instance
        self.position = - 1

    def __next__(self):
        self.position += 1
        if self.position < len(self.intstance):
            return self.intstance[self.position]
        else:
            raise StopIteration
    

class Tasks:
    def __init__(self) -> None:
        self._tasks = []

    def __getitem__(self, index):
        return self._tasks[index]
    
    def _iter_(self):
        return Iterator(self)
    
    def __len__(self):
        return len(self._tasks)
    
    def add_task(self, task: 'Task'):
        self._tasks.append(task)

    def list_tasks(self):
        for index, task in enumerate(self._tasks, start=1):
            task_name = task['name']
            task_status = task['status']
            print(f'{index}. {task_name}; {task_status}')

    def help(self):
        print('help text')

    def get_user_input(self, message, converter=str):
        user_input = converter(input(message))
        return user_input
    
    def delete_task(self):
        item_to_remove = self.get_user_input('select numbers of the task to delete it: ', int)
        if 1 <= item_to_remove <= len(self._tasks):
            self._tasks.pop(item_to_remove - 1)


    def input_task_number(self):
        number = int(input('choose the number of the task: '))
        return number

    def input_task_name(self):
        name = str(input('choose a new task name: '))
        return name

    def replace_task_name(self):
        which_task = self.input_task_number()
        new_name = self.input_task_name()
        self._tasks[which_task - 1]['name'] = new_name


    def input_status_name(self):
        name = str(input('choose a new status name: '))
        return name

    def replace_task_status(self):
        which_task = self.input_task_number()
        new_status = self.input_status_name()
        self._tasks[which_task - 1]['status'] = new_status


    def save_to_disk(self):
        name = input('give your file a name: ')
        self.write_to_json(name)

    def write_to_json(self, name):
        with open(f'{name}.json', 'w') as to_drive:
            generated_json = json.dumps(self._tasks)
            to_drive.write(generated_json)
            to_drive.close()


    def read_from_disk(self):
        read = input('select a file to read from: ')
        self.read_from_json(read)

    def read_from_json(self, read):
        with open(read, 'r') as from_drive:
            to_load = from_drive.read()
            load_from_json = json.loads(to_load)
            print(load_from_json)
            from_drive.close()

class Task(Tasks):
    def __init__(self, name=None, status=None) -> None:
        self.name = name
        self.status = status

    def __repr__(self) -> str:
        return self.name, self.status

    def new_task_input(self):
        user_input = input('enter task name: ')
        self.name = user_input
        self.status = 'new'
        return self.name, str(self.status)

    def __str__(self):
        return f'{self.name} ({self.status})'

    def convert_to_dict(self) -> dict:
        return {'name': self.name, 'status': self.status}

    

tasks = []
tsk = Tasks()
task = Task()
while True:
    choose = input('choose and action: ')
    if choose == 'help':
        tsk.help()
    elif choose == 'add':
        input_task = task.new_task_input()
        converted_input_task = task.convert_to_dict()
        tsk.add_task(converted_input_task)
    elif choose == 'list':
        tsk.list_tasks()
    elif choose == 'delete':
        tsk.delete_task()
    elif choose == 'replace name':
        tsk.replace_task_name()
    elif choose == 'replace status':
        tsk.replace_task_status()
    elif choose == 'save':
        tsk.save_to_disk()
    elif choose == 'read':
        tsk.read_from_disk()
    elif choose == 'exit':
        exit()
    elif choose == 'quit':
        exit()
    else:
        print('unknown command; ')