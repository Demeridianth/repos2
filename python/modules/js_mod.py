import json
import requests

# simple serialization example

# data = {
#     'president': {
#         'name': 'Zaphod Bebblobox',
#         'species': 'Betelgesian'
#     }
# }

# with open('data_file.json', 'w') as write_json:
#     json.dump(data, write_json, indent=4)

# with open('data_file.json', 'r') as read_file:
#     data =  json.load(read_file)

# print(data)


# DUMPS writes it to native Python string object: IF YOU NEED TO USE IT LATER IN THE PROGRAMM!

# json_string = json.dumps(data, indent=4)

# print(json_string)

# data = json.loads(json_string)

# print(data)





"""Manipulate the JSON data as a normal Python object!"""

# https://jsonplaceholder.typicode.com/


response = requests.get("https://jsonplaceholder.typicode.com/todos")  #  STILL NEED TO LEARN REQUESTS !
todos = json.loads(response.text)


# userId to number of complete TODOs for that user
todos_by_user = {}

# complete TODOs for each user
for todo in todos:
    if todo['completed']:
        try:
            todos_by_user[todo['userId']] += 1
        except KeyError:
            # this user has not been seen. Set count to 1
            todos_by_user[todo['userId']] = 1


# Sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)    # DONT KNOW HOW EXACTLY THIS WORKs :D LAMBDA !!!


# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]


# List of all users who have completed the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = ' and '.join(users)



# Create a JSON file that contains the completed TODOs for each of the users who completed the maximum number of TODOs.

# Function to filter out completed TODOs of users with max completed TODOs.
def keep(todo):
    is_complete = todo['completed']
    has_max_count = str(todo['userId']) in users
    return is_complete and has_max_count

# Write to file
with open('filtered_data_file.json', 'w') as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)







"""Encoding and Decoding Custom Python Objects"""

class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]


elf = Elf(level=4)
# >>> json.dumps(elf)
# TypeError: Object of type 'Elf' is not JSON serializable




"""Simplifying Data Structures"""

# Python has a built-in type called complex for representing complex numbers

# z = 3 + 8j
# >>> type(z)
# <class 'complex>

# >>> z.real
# 3.0
# >>> z.imag
# 8.0

# >>> complex(3, 8)
# True



"""Encoding Custom Types"""

# To translate a custom object into JSON, you need to do is provide an encoding function to the dump() method’s default parameter.

### decoding function example (IS IT GOOD??????):

def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")


# The other common approach is to take JSONEncoder and override its default() method:

class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)
        


#  USING CLS PARAMETER
# >>> json.dumps(2 + 5j, cls=ComplexEncoder)
# '[2.0, 5.0]'

# OR CREATING AN OBJECT
# >>> encoder = ComplexEncoder()
# >>> encoder.encode(3 + 6j)
# '[3.0, 6.0]'




"""Decoding Custom Types"""

# This is what happens when you try encoding a complex number with the ComplexEncoder and then decoding the result:

# >>> complex_json = json.dumps(4 + 17j, cls=ComplexEncoder)
# >>> json.loads(complex_json)
# [4.0, 17.0]  RETURNS A LIST, BECAUSE ITS MISSING THE METADATA




# FILE complex_data.json:
# {
#     "__complex__": true,                    - "__complex__" key is the metadata (information about the type)
#     "real": 42,
#     "imag": 36
# }


# function to verify the key:
def decode_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


with open('complex_data.json') as complex_data:
    data = complex_data.read()
    z = json.loads(data, object_hook=decode_complex)     # decoding function

print(type(z))
print(z)

