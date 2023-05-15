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


    
# result[store][category][name][price]


result = {}

for data in marketplaces_data:
    store = data['name']
    if store not in result:
        result[store] = {}


    for product in data['products']:
        name = product['name']
        category = product['category']
        price = product['price']
        if category not in result[store]:
            result[store][category] = {}
        if name not in result[store][category]:
            result[store][category][name] = price


for store_name in result:
    print(f'{store_name}:')

    for category in result[store_name]:
        print(f'  {category}:')
        for product_name in result[store_name][category]:
            print(f'    {product_name} :{result[store_name][category][product_name]}')
                                               
         

    

    

    






 
    












    





    










    
        











































        





    

  

        












    









