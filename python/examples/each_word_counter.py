# Описание

# Напишите функцию count_word_occurrences, которая принимает на вход строку и возвращает словарь, содержащий количество каждого уникального слова в строке. При подсчете необходимо игнорировать регистр символов и знаки препинания.

# Примеры

# count_word_occurrences("Python is fun! Python is aboba.") # {'python': 2, 'is': 2, 'fun': 1, 'aboba': 1}



from collections import Counter
from string import punctuation


def count_word_occurrences(s: str) -> dict:
    for i in punctuation:
        s = s.replace(i, "")
    s = s.lower().split()
    return dict(Counter(s))


text = "Python is fun! Python is aboba."
print(count_word_occurrences(text))
