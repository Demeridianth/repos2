import json
marketplaces_data = [
    {
        'name': 'Amazon',
        'products': [
            {'name': 'iPhone 13', 'category': 'Smartphones', 'price': 700},
            {'name': 'iPhone 13 Pro', 'category': 'Smartphones', 'price': 1000},
            {'name': 'iPhone 13 Pro Max', 'category': 'Smartphones', 'price': 1300},
            {'name': 'Xbox Series S', 'category': 'Gaming Consoles', 'price': 400},
            {'name': 'XBox Series X', 'category': 'Gaming Consoles', 'price': 700},
            {'name': 'Sony Playstation 5', 'category': 'Gaming Consoles', 'price': 800},
        ]
    },

    {
        'name': 'Best Buy',
        'products': [
            {'name': 'iPhone 13', 'category': 'Smartphones', 'price': 700},
            {'name': 'iPhone 14', 'category': 'Smartphones', 'price': 900},
            {'name': 'iPhone 14 Pro', 'category': 'Smartphones', 'price': 1100},
            {'name': 'Sony Playstation 5', 'category': 'Gaming Consoles', 'price': 850},
            {'name': 'Nintendo Switch OLED', 'category': 'Gaming Consoles', 'price': 380},
        ]
    }
]


marketplaces_file = open('marketplaces.json', 'w')
generate_json = json.dumps(marketplaces_data)
marketplaces_file.write(generate_json)
marketplaces_file.close

marketplaces_file = open('marketplaces.json', 'r')
read_file = marketplaces_file.read()
marketplaces_file.close

into_python = json.loads(read_file)
print(into_python)










    





