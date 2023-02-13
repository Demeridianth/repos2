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
file.write('[')

first_name = f'"first-name"'
f_name = f'"Alex"'
last_name = f'"last-name"'
l_name = f'"Smith"'
emails = f'"emails"'

email_alex = f'"email"'
eml_alex = f'"alex.smith@company.local"'
alex_type = f'"type"'
alex_work = f'"work"'
Alex_Smith = {email_alex: eml_alex, alex_type: alex_work}

email_bunny = f'"email"'
eml_bunny = f'"funny-bunny@gmail.local"'
bunny_type = f'"type"'
bunny_personal = f'"personal"'
Funny_Bunny = {email_bunny: eml_bunny, bunny_type: bunny_personal}

inside_emails = [Alex_Smith, Funny_Bunny]

overall_dict = {first_name: f_name, last_name: l_name, emails: inside_emails}

overall = f'{overall_dict}'
overall = overall.replace("'", '')

file.write(overall)
file.write(']')

file.close()







