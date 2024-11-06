from collections import Counter
import re

def open_file(path: str) -> str:
    with open(path, 'r') as file:
        text = file.read()
        return text


def get_word_count(text: str) -> tuple[list[str, ]]:
    words = re.findall(r'\b\w+\b', text)
    word_count = Counter(words)
    return word_count.most_common(n=5)


def analyse(text: str) -> dict[str, int]:
    result = {
        'characters including spaces': len(text),
        'characters excluding spaces': len(text.replace(' ', '')),
        'spaces total': text.count(' ',),
        'words total': len(text.split())
    }
    return result


def main() -> None:
    text = open_file('note.txt')
    analysis = analyse(text)
    word_count_dict = get_word_count(text)
    word_count = ', '.join(f"{word}: {count}" for word, count in word_count_dict)
    print(f'the 5 most common words are: {word_count}')
    for key, value in analysis.items():
        print(f'This text file contains {value} {key}') 


if __name__ == '__main__':
    main()


    
"""
Homework:
1. Create a much more user friendly message regarding the analysis (eg. "This text file contains...").
2. Add the top 5 most common words to the analysis message.

"""