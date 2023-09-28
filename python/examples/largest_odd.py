i = 0
result = -1
while i <= 18:
    print(f'iter No{i} began, i = {i}')
    
    if i % 5 == 0:
        result = i
    
    i += 1
    print(f'Iter No{i} ended')
    
print(f'first odd number = {result}')

# first odd number = 15



# endless loop

i = 0
while i >= 0:
    i += 1
    result = i
    print(result)