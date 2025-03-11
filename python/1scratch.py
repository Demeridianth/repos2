import string
import random
from itertools import cycle

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


    # ENCRYPTORS


    # Vigenère Cipher

    # Instead of shifting characters by a fixed amount (like Caesar Cipher), the Vigenère Cipher shifts each letter based on a repeating      keyword. Each letter in the keyword determines the shift for the corresponding letter in the plaintext.

    def encrypt_vigenere_cipher(self, text: str, keyword: str) -> str:
        keyword_shift_list = [self.lower_letters.index(char) for char in keyword]
        iterated_shift_number = cycle(keyword_shift_list)
        encoded_text = []
        
        for char in text:
            # check for lower letters
            if char in self.lower_letters:
                new_index = self.lower_letters.index(char)
                encoded_text.append(self.lower_letters[(new_index + next(iterated_shift_number)) % len(self.lower_letters)])

            # check for upper letters
            elif char in self.upper_letters:
                new_index = self.upper_letters.index(char)
                encoded_text.append(self.upper_letters[(new_index + next(iterated_shift_number)) % len(self.upper_letters)])

            # check for digits
            elif char in self.digits:
                new_index = self.digits.index(char)
                encoded_text.append(self.digits[(new_index + next(iterated_shift_number)) % len(self.digits)])
            
            # keep spaces and punctuation as they were
            else:
                encoded_text.append(char)
        
        return ''.join(encoded_text)
    
    def decrypt_vigenere_cipher(self, encrypted_text, keyword):
        keyword_shift_list = [self.lower_letters.index(char) for char in keyword]
        iterated_shift_number = cycle(keyword_shift_list)
        decyrpted_text = []

        for char in encrypted_text:
            # check for lower letters
            if char in self.lower_letters:
                new_index = self.lower_letters.index(char)
                decyrpted_text.append(self.lower_letters[(new_index - next(iterated_shift_number)) % len(self.lower_letters)])

            # check for upper letters
            elif char in self.upper_letters:
                new_index = self.upper_letters.index(char)
                decyrpted_text.append(self.upper_letters[(new_index - next(iterated_shift_number)) % len(self.upper_letters)])

            # check for digits
            elif char in self.digits:
                new_index = self.digits.index(char)
                decyrpted_text.append(self.digits[(new_index - next(iterated_shift_number)) % len(self.digits)])

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
        result = []
        
        for char in text:
            # handle spaces and punctuation
            if char not in self.upper_lower_digits or char in self.punctuation:
                result.append(char)

            # replace character with a character from secret_key
            else:
                result.append(encryptor[char])

        return ''.join(result)
    

    def decrypt_secret_key(self, encrypted_text: str) -> str:
        random.seed(22)
        secret_key = ''.join(random.sample(self.upper_lower_digits, len(self.upper_lower_digits)))
        characters = self.upper_lower_digits
        decryptor = {secret_key[char]: characters[char] for char in range(len(secret_key))}
        result = []

        for char in encrypted_text:
            # handle spaces and punctuation
            if char not in secret_key or char in self.punctuation:
                result.append(char)

            # replace character with a character from self.upper_lower_digits
            else:
                result.append(decryptor[char])

        return ''.join(result)
    

ciphers = Ciphers()

# Tests
# print('Ceaser Cipher')
# result = ciphers.encrypt_ceaser_cipher('Encrypt this Text: 1 time !')
# print(result)
# back_result = ciphers.decrypt_ceaser_cipher(result)
# print(f'{back_result}\n')

# print('Secret Key')
# result = ciphers.encrypt_secret_key('Encrypt this Text: 1 time !')
# print(result)
# back_result = ciphers.decrypt_secret_key(result)
# print(f'{back_result}\n')

# print('Vigenere Cipher')
# result = ciphers.encrypt_vigenere_cipher('Encrypt this Text: 1 time !', keyword='python')
# print(result)
# back_result = ciphers.decrypt_vigenere_cipher(result, keyword='python')
# print(back_result)


# Logic
if __name__ == '__main__':
    while True:
        print('Welcome to "choose your Cipher programm"')
        user_cipher = ciphers.get_user_input('Select the number of your cipher: \n', int)
        print('1. Vigenere Cipher'); print('2. Ceaser Cipher'); print('3. Secret Key Cipher')
        
        if user_cipher == 1:
            keyword_text = ...




    
         

