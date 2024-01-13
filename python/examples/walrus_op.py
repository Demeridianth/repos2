# WALRUS operator
# ОПЕРАТОР МОРЖА - оператор который позволяет присваивать значение перемменной внутри выражения и использовать эту переменную в сомом выражении

# num = 5
# print(num)
# >>> 5

# print(num := 5)
# >>> 5


# value = input('enter text: ')

# while value != 'q':
#     print(value)
#     value = input('enter another text: ')

# while (value := input('input another text: ')) != 'q':
#     print(value)


my_list = [1, 2, 3, 4, 5]
total = 0
partial_sum = []

# for i in my_list:
#     total = total + i
#     partial_sum.append(total)

partial_sum = [total := total + i for i in my_list]

print(f'summ of the list elements: {total}\nresult list: {partial_sum}')