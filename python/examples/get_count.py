
def scramble(str1, str2):
    # dct = {char: str1.count(char) for char in str1}
    dct = {}
    for l in str1:
        dct[l] = dct.get(l, 0) + 1

    for l in str2:
        if l not in dct or dct[l] == 0:
            return False 
        else:
            dct[l] -= 1
    return True

assert scramble('roqodlw', 'worold') == True
assert scramble('katas', 'steak') == False



text = 'texxxt'
letter_count = {n: text.count(n) for n in text}

    
        






    

    