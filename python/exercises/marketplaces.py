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

#products['Amazon']['Gaming Consoles']







results = {}

for data in marketplaces_data:
    store_name = data['name']
    if store_name not in results:
        results[store_name] = {}

        for product in data['products']:
            name = product['name']
            category = product['category']
            price = product['price']

            if category not in results[store_name]:
                results[store_name][category] = {}

            if name not in results[store_name][category]:
                results[store_name][category][name] = price

market = open('market_results.json', 'w')
generate_json = json.dumps(results)
market.write(generate_json)
market.close()

market = open('market_results.json', 'r')
market_data =  market.read()
market.close()

read_json = json.loads(market_data)
print(read_json)


# for result in results:
#     print(result)

#     for category_name in results[result]:
#         print(f'   {category_name}')
#         for index, item_price in enumerate(results[result][category_name], start=1):
#             print(f'        {index}.{item_price}: {results[result][category_name][item_price]}')












            





        



    
        

 
    



        





    
        












