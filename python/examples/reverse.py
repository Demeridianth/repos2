#reverse string

def reverse_string(string):
    reversed_list = list(reversed(string))
    reversed_string = ''.join(reversed_list)
    return reversed_string

print(reverse_string('ab123'))


# reverse list

lst = [1, 2, 3]
lst.reverse()
print(lst)



# REVERSE RETURNS NONE !!!

lst = [1, 2, 3]
rev_list = lst.reverse()
print(rev_list) # WILL PRINT NONE