import string


class Encryptors:
    def __init__(self) -> None:
        self.symbols = list(string.ascii_lowercase + string.digits + string.punctuation)
        self.letters = list(string.ascii_lowercase)
        self.digits = list(string.digits)
        self.punctuation = list(string.punctuation)
        self.encoders = [1, 2, 3]

    @staticmethod
    def get_user_input(prompt: str, converter=str) -> str:
        return converter(input(prompt))


    # ENCRYPTORS

    # Ceaser Cipher
    def encrypt_ceaser_cipher(self, text: str) -> str:
        encoded_text = []
        for char in range(len(text)):
            # handle spaces and punctuation
            if text[char] not in self.symbols or text[char] in self.punctuation:
                encoded_text.append(text[char])

            # check for letters
            elif text[char] in self.letters:
                letters_index = self.letters.index(text[char])
                encoded_text.append(self.letters[letters_index - 3])

            # check for digits
            elif text[char] in self.digits:
                digit_index = self.digits.index(text[char])
                encoded_text.append(self.digits[digit_index - 3])
        return ''.join(encoded_text)
    
    def decrypt_ceaser_cipher(self, text: str) -> str:
        decoded_text = []
        for char in range(len(text)):
            # handle spaces and punctuation
            if text[char] not in self.symbols or text[char] in self.punctuation:
                decoded_text.append(text[char])

            # check for letters
            elif text[char] in self.letters:
                letters_index = self.letters.index(text[char])
                decoded_text.append(self.letters[(letters_index + 3) % len(self.letters)])

            # check for digits
            elif text[char] in self.digits:
                digit_index = self.digits.index(text[char])
                decoded_text.append(self.digits[(digit_index + 3) % len(self.digits)])
        return ''.join(decoded_text)


        


codes = Encryptors()
result = codes.encrypt_ceaser_cipher('Encrypt this Text: 1 time !')
print(result)
back_result = codes.decrypt_ceaser_cipher(result)
print(back_result)

# if __name__ == '__main__':
#     encoder_number = codes.get_user_input('choose your encoder number: 1. Ceaser Cipher\n, 2. ???\n, 3. ???')




    
         

