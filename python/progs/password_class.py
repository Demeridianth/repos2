import secrets
import string


class Password:
    def __init__(self, length: int = 12, uppercase: bool = True, symbols: bool = True) -> None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        # get characters from string module
        self.base_characters = string.ascii_lowercase + string.digits
        
        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols:
            self.base_characters += string.punctuation

    def generate(self) -> str:
        password = []
        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))
        return ''.join(password)
    

    def check_password(self) -> None:
        if self.length < 16:
            raise ValueError('Password is too short')
        if not self.use_uppercase:
            raise ValueError('uppercase turned off')
        if not self.use_symbols:
            raise ValueError('symbols turned ff')
        

def main() -> None:
    password = Password(length=20, uppercase=False, symbols=True)
    password.check_password() 
    for _ in range(10):
        generated = password.generate()
        print(f'{generated} ({len(generated)} chars)')
        return generated

if __name__ == '__main__':
    main()





    
