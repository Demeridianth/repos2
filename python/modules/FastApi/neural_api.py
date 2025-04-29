from pydantic import BaseModel, Field
from typing import List, Optional
from enum import IntEnum, Enum
from fastapi import FastAPI, HTTPException

# uvicorn neural_api:api --reload
# fastapi dev neural_api.py --port 9999
# http://127.0.0.1:8000/docs         for docs and UI
api = FastAPI()

# GET, POST, PUT, DELETE

# Enum in Python is used to define a fixed set of options with names and 
# values — like status codes, roles, days of the week, etc.
class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1


class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=512, description='Name of the todo')
    todo_description: str = Field(..., description='Description of the todo')
    priority: Priority = Field(default=Priority.LOW, description='Priority of the todo')


# not strictly neccesary but more shcema to validate response

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int = Field(..., description='Unique identifier of the todo')

# very useful, dont have to update everything
class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, min_length=3, max_length=512, description='Name of the todo')
    todo_description: Optional[str] = Field(None, description='Description of the todo')
    priority: Optional[Priority] = Field(None, description='Priority of the todo')

all_todos = [
    Todo(todo_id=2, todo_name='Clean house', todo_description='Cleaning House', priority=Priority.HIGH),
    Todo(todo_id=1, todo_name='Sports', todo_description='Go to the Gym', priority=Priority.MEDIUM),
    Todo(todo_id=3, todo_name='READ', todo_description='Read 5 chapters', priority=Priority.LOW),
    Todo(todo_id=4, todo_name='Work', todo_description='Complete Project', priority=Priority.MEDIUM),
    Todo(todo_id=5, todo_name='Study', todo_description='Prepare for exam', priority=Priority.LOW) 
]

@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail='Todo not found')


@api.get('/todos', response_model=List[Todo])
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
    

@api.post('/todos', response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1
    
    new_todo = Todo(
        todo_id = new_todo_id,
        todo_name = todo.todo_name,
        todo_description = todo.todo_description,
        priority = todo.priority)

    all_todos.append(new_todo)
    return new_todo


@api.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
        
    raise HTTPException(status_code=404, detail='Todo not found')    


@api.delete('/todos/{todo_id}', response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
        
    raise HTTPException(status_code=404, detail='Todo not found')



""" simple, not-pro API """

# all_todos = [
#     {'todo_id': 1, 'todo_name': 'Sports', 'todo_description:': 'Go to the Gym'},
#     {'todo_id': 2, 'todo_name': 'Read', 'todo_description:': 'Read 10 pages'},
#     {'todo_id': 3, 'todo_name': 'Shop', 'todo_description:': 'Go shopping'},
#     {'todo_id': 4, 'todo_name': 'Study', 'todo_description:': 'Study for exam'},
#     {'todo_id': 5, 'todo_name': 'Meditate', 'todo_description:': 'Meditate 20 minutes'}
# ]

# @api.get('/')
# def index():
#     return {'message': 'Hello World'}


# # path parameter
# @api.get('/todos/{todo_id}')
# def get_todo(todo_id: int):
#     for todo in all_todos:
#         if todo['todo_id'] == todo_id:
#             return {'result': todo}


# # quary parameter
# # localhost:9999/todos?first_n=3
# # need to spicify types, Fast Api uses Pydentic
# @api.get('/todos')
# def get_todos(first_n: int = None):
#     if first_n:
#         return all_todos[:first_n]
#     else:
#         return all_todos


# @api.post('/todos')
# def create_todo(todo: dict):
#     new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1
    
#     new_todo = {
#         'todo_id': new_todo_id,
#         'todo_name': todo['todo_name'],
#         'todo_description': todo['todo_description']
#     }

#     all_todos.append(new_todo)


# @api.put('/todos/{todo_id}')
# def update_todo(todo_id: int, updated_tod: dict):
#     for todo in all_todos:
#         if todo['todo_id'] == todo_id:
#             todo['todo_name'] = updated_tod['todo_name']
#             todo['todo_description'] = updated_tod['todo_description']
#             return todo
        

# @api.delete('/todos/{todo_id}')
# def delete_todo(todo_id: int):
#     for index, todo in enumerate(all_todos):
#         if todo['todo_id'] == todo_id:
#             deleted_todo = all_todos.pop(index)
#             return deleted_todo
#     return 'Error, not found'


