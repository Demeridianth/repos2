# Найти в списке целых числ numbers самое часто встречающееся число и вернуть
#     кортеж. в котором:
#     - первым элементом является это число
#     - вторым элементом является список индексов этих чисел в списке (в каких позициях
#       списка numbers это число встречалось).

def most_common_number(numbers):

    n1 = {}
    result_number = -1
    result_index = []

    for i in numbers:
        if i not in n1:
            n1[i] = 0
        n1[i] += 1

    for i in n1:
        for z in n1:
            if n1[i] > n1[z]:
                if n1[i] > result_number:
                    result_number = i

    for i in range(len(numbers)):
        if numbers[i] == result_number:
            result_index.append(i)

    result = (result_number, result_index)

    return result

print(most_common_number([1, 2, 2, 3, 3, 4, 5]))








    
        

































# def task_1(numbers: list[int], n: int) -> list[tuple[int, int]]:
    # """
    # Найти в списке целых чисел numbers все пары чисел, которые в сумме дают
    # значение n. Вернуть список, каждым элементом которого является кортеж из
    # двух элементов, содержащих индексы чисел в numbers, которые в сумме дают n.
    # [1, 2]

# def pairs_summ_to_n(numbers, n):
#     result = []

#     for i in range(len(numbers)):
#         for z in range(i + 1, len(numbers)):
#             if numbers[i] + numbers[z] == n:
#                 result.append((numbers[i], numbers[z]))

#     return result


# print(pairs_summ_to_n([1, 2, 3, 4, 5, 6, 7, 8], 8))



# assert pairs_summ_to_n([1, 2, 3, 4, 5, 6, 7, 8], 8) == [(2, 6)]






        





    

  

        












    









