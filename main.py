import speech_recognition as sr
from time import ctime
import webbrowser
import time
import os
import random
from gtts import gTTS
import playsound

r = sr.Recognizer()
r.energy_threshold = 2837
r.dynamic_energy_threshold = True

def record_audio(ask = False):
    if ask:
        alina_speak(ask)
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alina_speak("Sorry I did not get that")
        except sr.RequestError:
            alina_speak("Sorry my speech service is down")
        return voice_data

def alina_speak(audio_string):
    tts = gTTS(text=audio_string, tld='com', lang="en", slow=False)
    r = random.randint(1, 1000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    print(audio_string)
    playsound.playsound(audio_file)
    os.remove(audio_file)

def respond(voice_data):
    if "what is your name" in voice_data:
        alina_speak("My name is Alina")
    if "what time is it" in voice_data:
        alina_speak(ctime())
    if "search" in voice_data:
        search = record_audio("What do you want to search for?")
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        alina_speak("Here is what I found for " + search)
    if "find location" in voice_data:
        location = record_audio("What is the location?")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        alina_speak("Here is the location of " + location)
    if "exit" in voice_data:
        alina_speak("Goodbye!")
        exit()
    if "tell a joke" in voice_data:
        # importing installed library
        import pyjokes
        # using get_joke() to generate a single joke
        #language is english
        #category is neutral
        My_joke = pyjokes.get_joke(language="en", category="neutral")
        alina_speak(My_joke)
        
time.sleep(1)
alina_speak("How can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)
