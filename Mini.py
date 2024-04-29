from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play
import time

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

# Inverse Morse code dictionary
inverse_morse_code_dict = {value: key for key, value in morse_code_dict.items()}
/
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char == ' ':
            morse_code += ' '
        elif char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
    return morse_code.strip()

def morse_to_text(morse_code):
    text = ''
    for code in morse_code.split(' '):
        if code == '':
            text += ' '
        elif code in inverse_morse_code_dict:
            text += inverse_morse_code_dict[code]
    return text

def play_morse_code(morse_code):
    for code in morse_code:
        if code == '.':
            beep = Sine(1000).to_audio_segment(duration=100)
        elif code == '-':
            beep = Sine(1000).to_audio_segment(duration=300)
        elif code == ' ':
            time.sleep(0.3)  # Pause between characters
            continue
        play(beep)
        time.sleep(0.1)  # Pause between dots and dashes within a character

# Test the functions
input_text = "Signal And audio Processing"
morse_code = text_to_morse(input_text)
print("Text to Morse Code:", morse_code)

# output_text = morse_to_text(morse_code)
 #print("Morse Code to Text:", output_text)

play_morse_code(morse_code)