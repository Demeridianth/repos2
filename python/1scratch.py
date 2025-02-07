import random
import string


class Codes:
    def __init__(self) -> None:
        self.symbols = list(string.ascii_lowercase + string.digits + string.punctuation)
        self.letters = list(string.ascii_lowercase)
        self.digits = list(string.digits)
        self.punctuation = list(string.punctuation)
        self.encoders = []
        
    def encode_ceaser(self, text) -> None:
        encoded_text = []
        for i in range(len(text)):
            if text[i] not in self.symbols or text[i] in self.punctuation:
                encoded_text.append(text[i])
            elif text[i] in self.letters:
                letters_index = self.letters.index(text[i])
                encoded_text.append(self.letters[letters_index - 3])
        return encoded_text


codes = Codes()




    
         

