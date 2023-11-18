def is_palindrome(text1):
    for i in range(len(text1)):
        if i >= len(text1[- 1 - i]):
            break 
        if text1[i] != text1[- 1 - i]:
            return False
    return True

print(is_palindrome('bo'))



