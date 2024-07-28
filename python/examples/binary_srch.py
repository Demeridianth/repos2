looking_for = 3
numbers = [1, 2, 3, 4, 5, 7, 9, 10, 21, 45]

left_index = 0

right_index = len(numbers) - 1

middle_index = len(numbers) // 2

middle_number = numbers[middle_index]



def binary_s():
    if middle_number == looking_for:
        return middle_index
    elif middle_number > looking_for:
        right_index = middle_index - 1
    else:
        left_index = middle_index + 1
    result = middle_index        

    print(result)