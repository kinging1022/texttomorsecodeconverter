morse_code ={
    'a': '.-',     'b': '-...',   'c': '-.-.',   'd': '-..',    'e': '.',      'f': '..-.',
    'g': '--.',    'h': '....',   'i': '..',     'j': '.---',   'k': '-.-',    'l': '.-..',
    'm': '--',     'n': '-.',     'o': '---',    'p': '.--.',   'q': '--.-',   'r': '.-.',
    's': '...',    't': '-',      'u': '..-',    'v': '...-',   'w': '.--',    'x': '-..-',
    'y': '-.--',   'z': '--..',   '0': '-----',  '1': '.----', '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-', '"': '.-..-.', ':': '---...', ';': '-.-.-.', '-': '-....-',
    '_': '..--.-', '@': '.--.-.', '+': '.-.-.',  '=': '-...-',  '#': '-...-',  '$': '...-..-',
    '&': '.-...',  '%': '.-..-.'
}


def text_to_morse_code(text):
    code = []
    for letters in text:
        if letters.lower() in morse_code:
            code.append(morse_code[letters].lower())
        elif letters == '':
            code.append('/')

    return ''.join(code)

text_to_convert = input('what text do you want to convert to morse code: ')
morse_output = text_to_morse_code(text_to_convert)

print("The morse code is", morse_output)






