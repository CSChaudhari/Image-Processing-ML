from gtts import gTTS
import os
def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")
text_to_speech("Hello, Madam this is a text-to-speech Conversion")
