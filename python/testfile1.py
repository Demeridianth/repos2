



# def foo(d):
#     my_dict = {}
#     for key, value in d.items():
#         my_dict[value] = key
#     return my_dict    

# c = {'c': 3, 'd': 4, 'z': 5}    
# d = {'a': 1, 'b': 2}
# print(foo(c))

# def foo(l):
#     a = str(l)
#     b = a.replace('[', '').replace(']', '').split(', ')
 
#     c = []
#     for i in b:
#         if i != '':
#             c.append(int(i))
#     return c
    


# l = [['1', '2'], [], ['6', '7', '8']]

# print(foo(l))



# def foo(l):
#     my_list = []
#     for i in l:
#         for a in i:
#             my_list.append(a)
#     return my_list

# l = [[1, 4, 6], [], ['2', '6']]
# print(foo(l))


# def foo(n1, n2):
#     result = {}
#     index_to_key = {}

#     for index, key in enumerate(n1):
#         index_to_key[index] = key

#     for index, value in enumerate(n2):
#         key = index_to_key[index]
#         result[key] = value 

#     return result


# def foo(keys, values):
#     result = {}
#     for i in range(len(keys)):
#         key = keys[i]
#         value = values[i]
#         result[key] = value
        
#     return result




# n1 = [1, 2, 3]
# n2 = ['a', 'b', 'c']

# print(foo(n1, n2))


def foo(numbers1, numbers2):
    result = []
    for i in numbers1:
        if i in numbers2:
            result.append(i)
    return result

numbers1 = [1, 2, 3]
numbers2 = ['a,', 2, 'c']

print(foo(numbers1, numbers2))














    






