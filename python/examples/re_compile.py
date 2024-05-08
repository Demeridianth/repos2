import re
import sys


str1 = "Emma's luck numbers are 251 761 231 451"

pattern = r'\d{3}'
# d = match any digit from 0 to 9 in a target string
# 3  = inside curly braces mean the digit has to occur exactly three times in a row inside the target string.

regex_pattern = re.compile(pattern)

result = regex_pattern.findall(str1)
print(result)
# >>> ['251', '761', '231', '451']




find_any_word = re.compile(r'\w+')

any_word = find_any_word.findall(str1)
print(any_word)
# >>> ['Emma', 's', 'luck', 'numbers', 'are', '251', '761', '231', '451']





