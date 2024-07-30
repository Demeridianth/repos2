# conditional expression
x = 1
a = '1' if x == 1 else False
print(a)
# >>> 1



a = 10 if 0 else 5

# same as:

if 0:
    a = 10
else:
    a = 5
