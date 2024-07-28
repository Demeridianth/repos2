""" Unicode Text Versus Bytes """


s = 'café'
len(s)
# >>> 4

b = s.encode('utf8')
# >>> b'caf\xc3\xa9'
len(b)
# >>> 5
# bytes b has five bytes (the code point for “é” is encoded as two bytes in UTF-8).
b.decode()
# >>> 'café'



cafe = bytes('café', encoding='utf_8')
# >>> b'caf\xc3\xa9'
cafe[0]
# >>> 99
cafe[1:]
# >>> b'c'
# The fact that my_bytes[0] retrieves an int but my_bytes[:1]
# returns a bytes sequence of length 1 is only surprising because we
# are used to Python’s str type, where s[0] == s[:1]. For all other
# sequence types in Python, 1 item is not the same as a slice of
# length 1.


cafe_arr = bytearray(cafe)
# >>> bytearray(b'caf\xc3\xa9')
cafe_arr[-1:]
# >>> bytearray(b'\xa9')


# encoders/decoders

for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

# latin_1 b'El Ni\xf1o'
# utf_8   b'El Ni\xc3\xb1o'
# utf_16  b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'



# Coping with UnicodeEncodeError

# >>> city = 'São Paulo'
# >>> city.encode('utf_8')
# b'S\xc3\xa3o Paulo'
# >>> city.encode('utf_16')
# b'\xff\xfeS\x00\xe3\x00o\x00 \x00P\x00a\x00u\x00l\x00o\x00'
# >>> city.encode('iso8859_1')
# b'S\xe3o Paulo'
# >>> city.encode('cp437')
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "/.../lib/python3.4/encodings/cp437.py", line 12, in encode
#  return codecs.charmap_encode(input,errors,encoding_map)
# UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in
# position 1: character maps to <undefined>
# >>> city.encode('cp437', errors='ignore')
# b'So Paulo'
# >>> city.encode('cp437', errors='replace')
# b'S?o Paulo'
# >>> city.encode('cp437', errors='xmlcharrefreplace')
# b'S&#227;o Paulo'


"""How do you find the encoding of a byte sequence? Short answer: you can’t. You must be told."""


# ASCII (American Standard Code for Information Interchange), which encodes 128 specified characters into seven-bit integers.

# Unicode, which provides a unique number for every character, no matter the platform, program, or language, and is capable of representing all the characters used in the world's writing systems.

# UTF-8, a variable-width character encoding capable of encoding all 1,107,616 valid character code points in Unicode using one to four one-byte (8-bit) units.


# 170