
def if_anagram(text1, text2):
    for i in text2:
        if i not in text1:
            return False
    return True
    
    t1 = {}
    t2 = {}
    for i in text1:
        if i not in t1:
            ti[i] = 1
        else:
            t1[i] += 1

    for i in text2:
        if i not in t2:
            t2[i] = 1
        else:
            t2[i] += 1
    
    if t1 == t2:
        return True
    else:
        return False

print(if_anagram('some', 'smos'))

        












    









