numbers = [1, 2, 3, 4, 5, 6, 9]
result = None
i = 0

for current_number in numbers:
    if current_number > 0 and current_number % 3 == 0:
        result = current_number

print(f'Result = {result}')

# result = 9