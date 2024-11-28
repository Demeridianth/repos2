import random
import string
import secrets


# with random
def generate_password_random(length: int = 10) -> str:
    symbols = string.ascii_lowercase + string.digits
    chosen = random.sample(symbols, length)
    password = [n for n in chosen]
    return ''.join(password)


# with secrets
def generate_password_secrets(length: str = 10) -> str:
    symbols = string.ascii_lowercase + string.digits
    password = [secrets.choice(symbols) for i in range(length)]
    return ''.join(password)


def main():
    generate_password_random()
    generate_password_secrets()

