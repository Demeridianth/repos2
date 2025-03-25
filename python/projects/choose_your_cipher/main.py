import string
import random
from itertools import cycle
from flask import Flask, request, render_template

app = Flask(__name__)


""" Program that let's the user choose a cipher out of 3 different ones (Vigenere Cipher, Ceaser Cipher, Secret Key cipher) 
to encode the text of user's choosing and decode it back """


class Ciphers:
    def __init__(self) -> None:
        self.lower_letters = list(string.ascii_lowercase)
        self.upper_letters = list(string.ascii_uppercase)
        self.digits = list(string.digits)
        self.upper_lower_digits = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
        self.punctuation = list(string.punctuation)
        
    @staticmethod
    def get_user_input(prompt: str, converter=str) -> str:
        return converter(input(prompt))


    # Vigenère Cipher

    # Instead of shifting characters by a fixed amount (like Caesar Cipher), the Vigenère Cipher shifts each letter based on a repeating      keyword. Each letter in the keyword determines the shift for the corresponding letter in the plaintext.

    def encrypt_vigenere_cipher(self, text: str, keyword: str) -> str:
        keyword_shift_list = [self.lower_letters.index(char) for char in keyword]
        iterated_shift_number = cycle(keyword_shift_list)
        encoded_text = []
        
        for char in text:
            try:
                shift = next(iterated_shift_number)
            except StopIteration:
                break
                

            # check for lower letters
            if char in self.lower_letters:
                new_index = self.lower_letters.index(char)
                encoded_text.append(self.lower_letters[(new_index + shift) % len(self.lower_letters)])

            # check for upper letters
            elif char in self.upper_letters:
                new_index = self.upper_letters.index(char)
                encoded_text.append(self.upper_letters[(new_index + shift) % len(self.upper_letters)])

            # check for digits
            elif char in self.digits:
                new_index = self.digits.index(char)
                encoded_text.append(self.digits[(new_index + shift) % len(self.digits)])
            
            # keep spaces and punctuation as they were
            else:
                encoded_text.append(char)
        
        return ''.join(encoded_text)
    
    def decrypt_vigenere_cipher(self, encrypted_text, keyword):
        keyword_shift_list = [self.lower_letters.index(char) for char in keyword]
        iterated_shift_number = cycle(keyword_shift_list)
        decyrpted_text = []

        for char in encrypted_text:
            try:
                shift = next(iterated_shift_number)
            except StopIteration:
                break

            # check for lower letters
            if char in self.lower_letters:
                new_index = self.lower_letters.index(char)
                decyrpted_text.append(self.lower_letters[(new_index - shift) % len(self.lower_letters)])

            # check for upper letters
            elif char in self.upper_letters:
                new_index = self.upper_letters.index(char)
                decyrpted_text.append(self.upper_letters[(new_index - shift) % len(self.upper_letters)])

            # check for digits
            elif char in self.digits:
                new_index = self.digits.index(char)
                decyrpted_text.append(self.digits[(new_index - shift) % len(self.digits)])

            # keep spaces and punctuation as they were
            else:
                decyrpted_text.append(char)

        return ''.join(decyrpted_text)


    # Ceaser Cipher

    def encrypt_ceaser_cipher(self, text: str) -> str:
        encoded_text = []
        for char in text:
            # check for lowercase letters
            if char in self.lower_letters:
                letters_index = self.lower_letters.index(char) 
                encoded_text.append(self.lower_letters[letters_index - 3]) 

            # check for uppercase letters
            elif char in self.upper_letters:
                letters_index = self.upper_letters.index(char) 
                encoded_text.append(self.upper_letters[letters_index - 3]) 

            # check for digits
            elif char in self.digits:
                digit_index = self.digits.index(char) 
                encoded_text.append(self.digits[digit_index - 3]) 

            else:
                encoded_text.append(char)
        return ''.join(encoded_text)
    

    def decrypt_ceaser_cipher(self, text: str) -> str:
        decoded_text = []
        for char in text:
            # check for upper letters:
            if char in self.upper_letters:
                letters_index = self.upper_letters.index(char)
                decoded_text.append(self.upper_letters[(letters_index + 3) % len(self.lower_letters)])

            # check for lower letters
            elif char in self.lower_letters:
                letters_index = self.lower_letters.index(char)
                decoded_text.append(self.lower_letters[(letters_index + 3) % len(self.lower_letters)])

            # check for digits
            elif char in self.digits:
                digit_index = self.digits.index(char)
                decoded_text.append(self.digits[(digit_index + 3) % len(self.digits)])

            else:
                decoded_text.append(char)
        return ''.join(decoded_text)


    # Secret Key Cipher

    def encrypt_secret_key(self, text: str) -> str:
        random.seed(22)
        secret_key = ''.join(random.sample(self.upper_lower_digits, len(self.upper_lower_digits)))
        characters = self.upper_lower_digits
        encryptor = {characters[char]: secret_key[char] for char in range(len(characters))}
        result = [encryptor.get(char, char) for char in text]

        return ''.join(result)
    

    def decrypt_secret_key(self, encrypted_text: str) -> str:
        random.seed(22)
        secret_key = ''.join(random.sample(self.upper_lower_digits, len(self.upper_lower_digits)))
        characters = self.upper_lower_digits
        decryptor = {secret_key[char]: characters[char] for char in range(len(secret_key))}
        result = [decryptor.get(char, char) for char in encrypted_text]

        return ''.join(result)
    

ciphers = Ciphers()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        text = request.form['text']
        keyword = request.form.get('keyword', '')
        cipher_type = request.form['cipher_type']
        action_type = request.form.get('action_type', '')

        if cipher_type == 'vigenere':
            if action_type == 'encrypt':
                result = ciphers.encrypt_vigenere_cipher(text, keyword)
            elif action_type == 'decrypt':
                result = ciphers.decrypt_vigenere_cipher(text, keyword)
        if cipher_type == 'ceaser':
            if action_type == 'encrypt':
                result = ciphers.encrypt_ceaser_cipher(text)
            elif action_type == 'decrypt':
                result = ciphers.decrypt_ceaser_cipher(text)   
        if cipher_type == 'secret':
            if action_type == 'encrypt':
                result = ciphers.encrypt_secret_key(text)
            elif action_type == 'decrypt':
                result = ciphers.decrypt_secret_key(text)

    return render_template('index.html', result=result)
        
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)


# http://127.0.0.1:5000/
    
            
            





    
         

