from gtts import gTTS
import os
from gtts.lang import tts_langs

def text_to_audio(text, filename="suresh.txt"):
    # Convert text to speech
    tts = gTTS(text=filename, lang='te')
    # Save the audio file
    tts.save(filename)
    print(f"Audio saved as {filename}")

text_to_audio("where are you", "hello.mp3")
#print(tts_langs())
