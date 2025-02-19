message = "hello"
shift = 3

# Encrypt
encrypted = "".join(chr(ord(char) + shift) for char in message)
print(encrypted)  # Output: 'khoor'

# Decrypt
decrypted = "".join(chr(ord(char) - shift) for char in encrypted)
print(decrypted)  # Output: 'hello'