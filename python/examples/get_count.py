from collections import Counter
from string import punctuation
import re


text = 'In a small town, there was a park where children played every day. The park was filled with trees and flowers. The children loved to run around the playground, swinging and sliding with joy. On sunny days, the park would be bustling with laughter and fun. Parents often gathered on benches, watching their children while enjoying the fresh air.Every weekend, the townspeople would organize events in the park. There were picnics, games, and music that brought everyone together. The community spirit was strong, and people looked forward to these gatherings. Some would bring homemade food, while others would prepare delicious treats to share.As the seasons changed, the park transformed. In spring, flowers bloomed, painting the landscape with vibrant colors. Summer brought warmth and long days, perfect for outdoor activities. Autumn showcased beautiful leaves, and winter turned the park into a snowy wonderland.'


# without libraries
split_text = text.split()
word_count = {}

for word in split_text:
    n = 1
    if word in word_count:
        word_count[word] = n + 1
    else:
        word_count[word] = n

largest_value = 0
most_common_key = None

for _ in range(5):
    # for key, value in word_count.items():
    #     if value > largest_value:
    #         most_common_key = key
    max_key = max(word_count, key=word_count.get)

    print(most_common_key)
    word_count.pop(most_common_key)



# with re
def get_frequency(text: str) -> list[tuple[str, ]]:
    words = re.findall(r'\b\w+\b', text)
    word_counts = Counter(words)
    return word_counts.most_common(n=5)



# with punctuation library
def count_word_occurrences(s: str) -> dict:
    for i in punctuation:
        s = s.replace(i, "")
    s = s.lower().split()
    return dict(Counter(s))

print(count_word_occurrences(text))


















# def scramble(str1, str2):
#     # dct = {char: str1.count(char) for char in str1}
#     dct = {}
#     for l in str1:
#         dct[l] = dct.get(l, 0) + 1

#     for l in str2:
#         if l not in dct or dct[l] == 0:
#             return False 
#         else:
#             dct[l] -= 1
#     return True

# assert scramble('roqodlw', 'worold') == True
# assert scramble('katas', 'steak') == False



# text = 'texxxt'
# letter_count = {n: text.count(n) for n in text}

    
        






    

    