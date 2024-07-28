dct = {'name': 'Joe', 'last_name': 'Rogan'}

a = dct.setdefault('name', 'Bob')
# >>> 'Joe'
b = dct.setdefault('age', 52)
# >>> 52
dct
# {'name': 'Joe', 'last_name': 'Rogan', 'age': 52