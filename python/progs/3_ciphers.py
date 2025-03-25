import string
import random
from itertools import cycle


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
        result = [encryptor.get(char, char) for char in text]

        return ''.join(result)
    

    def decrypt_secret_key(self, encrypted_text: str) -> str:
        random.seed(22)
        secret_key = ''.join(random.sample(self.upper_lower_digits, len(self.upper_lower_digits)))
        characters = self.upper_lower_digits
        decryptor = {secret_key[char]: characters[char] for char in range(len(secret_key))}
        result = [decryptor.get(char, char) for char in encrypted_text]

        return ''.join(result)
    

def main():
    ciphers = Ciphers()
    print('Welcome to "choose your Cipher program"')
    while True:
        print('1. Vigenere Cipher'); print('2. Ceaser Cipher'); print('3. Secret Key Cipher'); print('4. Quit the programm')
        user_cipher_choice = ciphers.get_user_input('Select the number of your cipher: ', int)
        
        if user_cipher_choice == 1:
            text = ciphers.get_user_input('Enter the text for the cipher to encode: ')
            keyword = ciphers.get_user_input('Enter the keyword for the cipher to use: ')
            encoded_result = ciphers.encrypt_vigenere_cipher(text, keyword)
            print(f'Your text have been encrypted to: "{encoded_result}"')
            decoding_user_choice = ciphers.get_user_input('Do you wish to decode the result back? (y/n): \n')
            if decoding_user_choice == 'y':
                decoded_result = ciphers.decrypt_vigenere_cipher(encoded_result, keyword)
                print(f'Your text have been decoded back to: "{decoded_result}"\n')
            else:
                continue
            
        elif user_cipher_choice == 2:
            text = ciphers.get_user_input('Enter the text for the cipher to encode: ')
            encoded_result = ciphers.encrypt_ceaser_cipher(text)
            print(f'Your text have been encrypted to: "{encoded_result}"')
            decoding_user_choice = ciphers.get_user_input('Do you wish to decode the result back? (y/n): \n')
            if decoding_user_choice == 'y':
                decoded_result = ciphers.decrypt_ceaser_cipher(encoded_result)
                print(f'Your text have been decoded back to: "{decoded_result}"\n')
            else:
                continue

        elif user_cipher_choice == 3:
            text = ciphers.get_user_input('Enter the text for the cipher to encode: ')
            encoded_result = ciphers.encrypt_secret_key(text)
            print(f'Your text have been encrypted to: "{encoded_result}"')
            decoding_user_choice = ciphers.get_user_input('Do you wish to decode the result back? (y/n): \n')
            if decoding_user_choice == 'y':
                decoded_result = ciphers.decrypt_secret_key(encoded_result)
                print(f'Your text have been decoded back to: "{decoded_result}"\n')
            else:
                continue

        else:
            break


if __name__ == '__main__':
    main()
    
            
            





    
         

