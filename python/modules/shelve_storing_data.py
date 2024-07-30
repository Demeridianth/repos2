import shelve

# saving data
with shelve.open('data') as shelf:
    shelf['key'] = 'this is stored in shelf data'

# reading data
with shelve.open('data') as shelf:
    print(shelf['key'])


# shelve is written in Picke and should be used in small projects only