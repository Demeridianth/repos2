from collections import Counter
import re
from pathlib import Path
from docx import Document
from PyPDF2 import PdfReader

def get_frequency(text: str) -> list[tuple[str, ]]:
    words = re.findall(r'\b\w+\b', text)
    word_counts = Counter(words)
    return word_counts.most_common(n=5)


def get_text() -> str:
    # docx file
    # file_path = Path('/mnt/c/Users/user/Downloads/word_text.docx')
    # doc = Document(file_path)
    # result = '\n'.join([para.text for para in doc.paragraphs])
    # return result

    # text file
    # file_path = Path.cwd() / 'about.txt'
    # # with file_path.open() as text:
    # #     result = text.read()
    # # same as:
    # result = file_path.read_text()
    # return result

    # pdf file
    file_path = Path('/mnt/c/users/user/downloads/Lorem_ipsum.pdf')
    pdf_reader = PdfReader(file_path)
    
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def main() -> None:
    
    word_frequancies = get_frequency(get_text())
    

    for word, count in word_frequancies:
        print(f'{word}: {count}')


if __name__ == '__main__':
    main()