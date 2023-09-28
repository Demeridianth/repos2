positive_numbers = [1, 2, 3, 4, 5, 7, 9]
i = 0
result = -1

while i < len(positive_numbers):
    
    current_number = positive_numbers[i]
    if current_number > 0 and current_number % 3 == 0:
        result = current_number

    i += 1

print(f'Result = {result}')