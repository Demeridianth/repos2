



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





#1

# def foo(numbers1, numbers2):
#     result = []
#     for i in numbers1:
#         if i in numbers2:
#             result.append(i)
#     return result

# numbers1 = [1, 2, 3]
# numbers2 = [2, 5, 'c']

# print(foo(numbers1, numbers2))

# 2

# def foo(numbers1, numbers2):
#     result = []
#     for i in numbers1:
#         for a in numbers2:
#             if i == a:
#                 result.append(i)
#     return result

# numbers1 = [1, 2, 3]
# numbers2 = [2, 5, 'c']

# print(foo(numbers1, numbers2))






# 1. Написать функцию, которая принимает список и проверяет, все
# ли элементы второго списка содержатся в первом
# def contains(a, b):
    # Например:
    # a = [1, 2, 3, 4]
    # b = [1, 2]
    # с = [1, 3, 8]
    # contains(a, b) возвращает True
    # contains(a, c) возвращает False

# def contains(a, b):
#     for i in b:
#         if i not in a:
#             return False
#     return True

           
# a = []
# b = []
# c = [1, 2, 8]

# print(contains(a, b))







# 2. Написать функции для шифрования и дешифрования сообщения
# def encrypt_message(message, secret_key):
#     message - сообщение строчными буквами, которое нужно 
#     зашифровать
    
#     secret_key - строка из 26 уникальных непробельных 
#     символов, которыми нужно заменять соответствующие 
#     (по порядковому номеру) буквы английского алфавита.
    
#     Другими словами, первым символом из secret_key мы будем 
#     заменять букву "a", второй - букву b и так далее
#     Например для message "i am a dog" и 
#     и secret_key "rmneabghxjcdfiopktulqwzysv"
#     получится "h xf x nob"

# def decrypt_message(encrypted_message, secret_key):
#     обратная операция

# def encrypt_message(message, secret_key):
#     alph = 'abcdefghijklmnopqrstuvwxyz'
    
#     encrypt = {}
#     result = []
 
#     for i in range(len(alph)):
#         key = alph[i]
#         value = secret_key[i]
#         encrypt[key] = value
   
#     for i in message:
#         if i not in alph:
#             result.append(i) 
#         else:
#             result.append(encrypt[i])
        
#     return ''.join(result)


# def decrypt_message(encrypted_message, secret_key):
#     alph = 'abcdefghijklmnopqrstuvwxyz'
#     decrypt = {}
#     result = []

#     for i in range(len(secret_key)):
#         key = secret_key[i]
#         value = alph[i]
#         decrypt[key] = value

#     for i in encrypted_message:
#         if i not in secret_key:
#             result.append(i)
#         else:
#             result.append(decrypt[i])
#     return ''.join(result)

# secret_key = "rmneabghxjcdfiopktulqwzysv"
# message = '1, 2, 3, 4'
# a = encrypt_message(message, secret_key)
# print(a)
# b = decrypt_message(a, secret_key)
# print(b)


    

    # ****************************************





# def by_numbers(str1, str2):
#     numbers = []
#     for i in range(len(str1)):
#         numbers.append(str1[i])
#         numbers.append(str2[i])
#     return ''.join(numbers)

# print(by_numbers('1', '2'))



# def by_numbers(str1, str2):
#     numbers = []
#     str2_slice = str2[::-1]
#     for i in range(len(str1)):
#         numbers.append(str1[i])
#         numbers.append(str2_b[i])
#     return ''.join(numbers)

# print(by_numbers('1234', '6789'))



# def all_even(numbers):

    # for i in numbers:
    #     if i % 2 == 0:
    #         continue
    #     else:
    #         return False
    # return True

    
#     if numbers == []:
#         raise ValueError
#     for i in numbers:
        

#         if i % 2 != 0:
#             return False
        
#     return True


# print(all_even([]))



# def if_palindrome(text):
#         text_back = text[::-1]
#         for i in range(len(text)):
#             if text[i] != text_back[i]:
#                 return False
#         return True


# text = 'abz1zba'
# print(if_palindrome(text))



# Проверить, что строка text2 является анаграммой строки text1. Другими
#     словами, проверить что text2 можно получить, переставив порядок букв в text1.

#     >>> check_is_anagram('', '')
#     True

#     >>> check_is_anagram('a', 'a')
#     True

#     >>> check_is_anagram(ab', 'ab')
#     True

#     >>> check_is_anagram('ab', 'ba')
#     True

#     >>> check_is_anagram('a', 'b')
#     False

#     >>> check_is_anagram('abbc', 'abcc')
#     False

#sorted()????????

def if_anagram(text1, text2):
    # if len(text1) != len(text2):
    #     return False
    
    # for i in text2:
    #     if i not in text1:
    #         return False 
    
    t1 = {}
    t2 = {}
    for i in text1:
        if i in t1:
            t1[i] += 1
        else:
            t1[i] = 1
    
    for i in text2:
        if i in t2:
            t2[i] += 1
        else: 
            t2[i] = 1

    if t1 == t2:
        return True
    else:
        return False

print(if_anagram('baba', 'abba'))






























    






