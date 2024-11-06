morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',     
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',  
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',   
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',     
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',  
    'Z': '--..',  '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',  
    '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',  
    '9': '----.',  ' ': '/',      '.': '.-.-.-', ',': '--..--', '?': '..--..',  
    "'": '.----.', '!': '-.-.--', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',  
    '&': '.-...',  ':': '---...', ';': '-.-.-.',  '=': '-...-',  '+': '.-.-.',  
    '-': '-....-', '_': '..--.-', '"': '.-..-.',  '$': '...-..-', '@': '.--.-.'
}

morse_code_flipped = {value: key for key, value in morse_code_dict.items()}


def convert_to_morse(text: str) -> str:
    return ' '.join(morse_code_dict.get(char.upper(), '') for char in text)


def convert_to_text(morse_code: str) -> str:
    return ''.join(morse_code_flipped.get(char).lower() for char in morse_code.split(' '))


def main() -> None:
    
    user_input = input('enter your text: ')
    output = convert_to_morse(user_input)
    flip_output = convert_to_text(output)
    print(output)
    print(flip_output)


if __name__ == '__main__':
    main()


"""
Homework:
1. Edit the program so that it also works with symbols, you're going to have
to do some research online and edit the dictionary.
2. Create a function that can convert the morse code back into regular text.

"""