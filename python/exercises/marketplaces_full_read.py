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

#results[store][category][name][price]

#write

marketplaces = open('marketplaces.txt', 'w')
for data in marketplaces_data:
    for product in data['products']:
        name = product['name']
        categoty = product['category']
        price = product['price']

        line = f'{name}:{categoty}:{price}\n'
        marketplaces.write(line)
marketplaces.close()


#read

            
marketplaces = open('marketplaces.txt', 'r')
marketplaces_info = []
products1 = []
lines = []
for i in range(6):
    lines.append(marketplaces.readline())
for line in lines:
    line = line.replace('/n', '')
    into_list = line.split(':')
    into_dict = {'name': into_list[0], 'category': into_list[1], 'price': int(into_list[2])}
    products1.append(into_dict)
print(products1)

marketplaces.close()







