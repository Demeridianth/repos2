marketplaces = [
    {'name': 'Amazon'}, 
    {'name': 'Best Buy'},
]

marketplaces = [
    {'name': 'Amazon'},
    {'name': 'Best Buy'},
]

products = [
    {'name': 'iPhone 13', 'category': 'Smartphones', 'price': 700},
    {'name': 'iPhone 14', 'category': 'Smartphones', 'price': 900},
    {'name': 'Sony Playstation 5', 'category': 'Gaming Consoles', 'price': 850},
    {'name': 'Nintendo Switch OLED', 'category': 'Gaming Consoles', 'price': 380},
    {'name': 'Xbox Series S', 'category': 'Gaming Consoles', 'price': 400},
    {'name': 'XBox Series X', 'category': 'Gaming Consoles', 'price': 700},
]

categories = []

for product in products:
    if product['category'] not in categories:
        categories.append(product['category'])

for category in categories:
    print(category)
    index = 1
    for product in products:
        if product['category'] == category:
            print(index, product['name'])
            index += 1

# print in list
    









categories = {}

for product in products:
    product_category = product['category']
    if product_category not in categories:
        categories[product_category] = []
    categories[product_category].append(product['name'])

for category in categories:  
     print(category)  
     index = 1  
     for product_name in categories[category]:  
         print(f'{index} {product_name}')  
     index += 1




    #print through index

for category in categories:  
     print(category)  
      
     for index, product_name in enumerate(categories[category]):  
         print(f'{index} {product_name}')  

    #print through enumerate BUT WILL START WITH 0
 



   

