import json

contacts = [
    {
        'first_name': 'Alex',
        'last_name': 'Smith',
        'emails': [
            {'email': 'alex.smith@company.local', 'type': 'work'},
            {'email': 'funny.bunny@gmail.local', 'type': 'personal'},
        ]
    }
]

#write
file = open('contacts.json', 'w')
generated_json = json.dumps(contacts)
file.write(generated_json)
file.close()

#read
file = open('contacts.json', 'r')
read_json = file.read()
file.close()

read_data = json.loads(read_json)
print(read_data)