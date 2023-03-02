from typing import Callable

# Функция должна принимать любой dict и возвращать dict,
    # в котором ключи и значения поменялись местами. 

# def foo(d):
#     my_dict = {}
#     for key, value in d.items():
#         my_dict[value] = key
#     return my_dict    

# c = {'c': 3, 'd': 4, 'z': 5}    
# d = {'a': 1, 'b': 2}
# print(foo(c))







  # Функция должна принимать список списков и объединять их в один

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









# Функция принимает два списка одной длины (это важно)
    # Возвращает словарь, в котором ключи - значения первого списка, значения - из второго

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




# Вернуть список чисел, которые есть и там и там
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




# Получает на вход две строки ОДИНАКОВОЙ длины n, text1 и text2 и возвращает
#     строку длины 2n, построенную по принципу:
#     - первый символ первой строки, первый символ второй строки
#     - второй символ первой строки, второй символ второй строки
#     - ...
#     - n-ный символ первый строки, n-ный элемент второй строки
# # def first_first(str1, str2):

#     numbers = []
#     for i in range(len(str1)):
#         numbers.append(str1[i])
#         numbers.append(str2[i])
#     return ''.join(numbers)

# print(by_numbers('1', '2'))






# Получает на вход две строки ОДИНАКОВОЙ длины n, text1 и text2 и возвращает
#     строку длины 2n, построенную по принципу:
#     - первый символ первой строки, n символ второй строки
#     - второй символ первой строки, n-1 символ второй строки
#     - ...
#     - n-ный символ первый строки, первый элемент второй строки


#1

# def first_last(str1, str2):
#     numbers = []
#     str2_b = str2[::-1]
#     for i in range(len(str1)):
#         numbers.append(str1[i])
#         numbers.append(str2_b[i])
#     return ''.join(numbers)

#2

# def first_last(str1, str2):
#     result = []

#     for i in range(len(str1)):
#         result.append(str1[i])
#         result.append(str2[ - 1 - i])
#     return ''.join(result)

# print(by_numbers('12', '34'))
# print(by_numbers('12', '34'))
# print(by_numbers('12', '34'))
# print(by_numbers('12', '34'))
# print(by_numbers('12', '34'))
# print(by_numbers('12', '34'))





# Получает на вход список целых чисел и возвращает True, если все они четные
#     и False в противном случае. Если передан пустой список, генерирует ValueError

#1:

# for i in numbers:
    #     if i % 2 == 0:
    #         continue
    #     else:
    #         return False
    # return True

#2:

# def all_even(numbers):
#     # if numbers == []:
#     if not numbers:
#         raise ValueError

#     for i in numbers:
#         if i % 2 != 0:
#             return False
        
#     return True


# print(all_even([2, 4]))



#  PALINDROME

# 1

# def is_palindrome(text):
#     text_length = len(text)
#     text_last_index = text_length - 1

#     for i in range(text_length):
#         left_char = text[i]
#         right_char = text[text_last_index - i]
#         if left_char != right_char:
#             return False

#     return True


# 2

# def is_palindrome(text):
#     text_length = len(text)
#     text_last_index = text_length - 1


#     for i in range(text_length):
#         left_index = i
#         right_index = text_last_index - i

#         if left_index >= right_index:
#             break

#         left_char = text[left_index]
#         right_char = text[right_index]
        
#         if left_char != right_char:
#             return False

#     return True


# print(is_palindrome(''))
# print(is_palindrome('a'))
# print(is_palindrome('aa'))
# print(is_palindrome('ab'))
# print(is_palindrome('aba'))
# print(is_palindrome('abb'))
# print(is_palindrome('abab'))
# print(is_palindrome('abba'))


   
# 3 (shortest)

# def if_palindrome(text1):

#     for i in range(len(text1)):
#    
#         if i >= len(text1[- 1 - i]):
#             break 

#         if text[i] != text[- 1 - i]:
#             return False
#     return True




# 4 (SLICE)

# def if_palindrome(text):
#     text_back = text[::-1]
#     for i in range(len(text)):
#         if text[i] != text_back[i]:
#             return False
#     return True


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

# def if_anagram(text1, text2):
    # if len(text1) != len(text2):
    #     return False
    
    # for i in text2:
    #     if i not in text1:
    #         return False 
    
    # t1 = {}
    # t2 = {}
    # for i in text1:
    #     if i in t1:
    #         t1[i] += 1
    #     else:
    #         t1[i] = 1
    
    # for i in text2:
    #     if i in t2:
    #         t2[i] += 1
    #     else: 
    #         t2[i] = 1

    # if t1 != t2:
    #     return False
    # return True


# def if_anagram(text1, text2):
#     t1 = {}
#     t2 = {}

#     for i in text1:
#         if i not in t1:
#             t1[i] = 0

#         t1[i] += 1 

    
#     for i in text2:
#         if i in t2:
#             t2[i] += 1
#         else: 
#             t2[i] = 1

#     if t1 != t2:
#         return False
#     return True


# print(if_anagram('baab', 'bbaa'))


# def pairs_to_n(numbers: list[int], n: int) -> list[tuple[int, int]]:
    # """
    # Найти в списке целых чисел numbers все пары чисел, которые в сумме дают
    # значение n. Вернуть список, каждым элементом которого является кортеж из
    # двух элементов, содержащих пары чисел в numbers, которые в сумме дают n.
    # [1, 2]

# def pairs_to_n(numbers, n):
#     result = []
#     for i in range(len(numbers)):
#         for z in range(i + 1, len(numbers)):
            
#             if numbers[i] + numbers[z] == n:
#                 result.append((numbers[i], numbers[z]))
#     return result

# assert pairs_to_n([50, 50, 20, 20], 100) == [(50, 50)]  

# assert pairs_to_n([50, 80, 3, 50, 20, 20], 100) == [(50, 50)] 
# assert pairs_to_n([50, 3, 50, 20, 20], 100) == [(50, 50)] 
# assert pairs_to_n([50, 3, 50, 20, 20], 100) == [(50, 50)] 





# def task_2(numbers: list[int]) -> tuple[int, list[int]]:
    
    # Найти в списке целых числ numbers самое часто встречающееся число и вернуть
    # кортеж. в котором:
    # - первым элементом является это число
    # - вторым элементом является список индексов этих чисел в списке (в каких позициях
    #   списка numbers это число встречалось).


# def most_common_number(numbers):
    # n1 = {}
    # result_number = 0
    # result_index = []

    # for i in numbers:
    #     if i not in n1:
    #         n1[i] = 0
    #     n1[i] += 1
    
    # for i in n1:
    #     for z in n1:
    #         if n1[i] > n1[z]:
    #             if n1[i] > result_number:
    #                 result_number = i
    
    # for index, number in enumerate(numbers):
    #     if number == result_number:
    #         result_index.append(index)

    # result = (result_number, result_index)
              
    # return result
   
# print(most_common_number([1, 2, 3, 3, 3]))
# print(most_common_number([1, 2, 2, 2, 3, 4]))
# print(most_common_number([1, 1, 1, 1, 1, 4, 5]))
# print(most_common_number([]))
# print(most_common_number([1, 2, 3, 4, 5]))
# print(most_common_number([1, 2, 2, 3, 3, 4, 5]))












    # def task_3(numbers: list[int], predicate: Callable[int, bool]) -> tuple[list[int], list[int]]:
    
    # Разделить список целых чисел numbers на два списка, используя предикат predicate.
    # Грубо говоря, функция должна принимать вторым аргументом другую функцию вида:
    #     def predicate(int) -> bool:
    #         ...
    # затем эта функция-предикат вызывается для каждого элемента numbers и те из них, для
    # которых функция-предикат вернула True попадают в один список, а те, для которых False -
    # в другой. В итоге возвращаем кортеж, в котором:
    # - первый элемент - список чисел из numbers, для которых предикат вернул True
    # - второй элемент - список чисел из numbers, для которых предикат вернул False
   

def to_predicate(numbers, predicate):
    def inner_func()

    



                
           





























    






