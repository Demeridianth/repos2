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


file = open('by_hand.json', 'w')
lines = []
for alt in contacts:
    first_name = alt['first_name']
    last_name = alt['last_name']
    line = f'[\n"first-name": "{first_name}",\n"last-name": "{last_name}",\n'
    
    file.write(line)

    for email in alt['emails']:
        lines.append(email)
        # line1 = f'{email}'
        line1 = f'"emails": [\n        {lines[0]},\n        {email}\n]'

    file.write(line1)

  
   

    

       

file.close()







