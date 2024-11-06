import random
import string
import secrets
import pytest


# with random
def generate_password_random(length: int = 10) -> str:
    symbols = string.ascii_lowercase + string.digits
    chosen = random.sample(symbols, length)
    password = [n for n in chosen]
    return ''.join(password)


# with secrets
def generate_password_secrets(length: str = 10) -> str:
    symbols = string.ascii_lowercase + string.digits
    password = [secrets.choice(symbols) for _ in range(length)]
    return ''.join(password)


# test
def test_generate_password_secrets() -> None:
    assert isinstance(generate_password_secrets(), str)


def main():
    generate_password_random()
    generate_password_secrets()

