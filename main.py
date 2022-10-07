import os
import random
import time
import webbrowser

from gtts import gTTS
import playsound
import pyjokes
import speech_recognition as sr
import wikipedia


# Initialize voice recognizer
r = sr.Recognizer()
r.energy_threshold = 2837
r.dynamic_energy_threshold = True


def record_audio(ask=False):
    if ask:
        alina_speak(ask)
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alina_speak("Sorry, I did not get that.")
        except sr.RequestError:
            alina_speak("Sorry, my speech service is down.")
        return voice_data


def alina_speak(audio_string):
    tts = gTTS(text=audio_string, tld="com", lang="en", slow=False)
    r = random.randint(1, 1000000)
    audio_file = f"audio-{str(r)}.mp3"
    tts.save(audio_file)
    print(audio_string)
    playsound.playsound(audio_file)
    os.remove(audio_file)


def respond(voice_data):
    voice_data = voice_data.lower()

    if "wikipedia" in voice_data:
        alina_speak("Searching wikipedia...")
        query = voice_data.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        alina_speak(results)
    if "what is your name" in voice_data:
        alina_speak("My name is Alina.")
    if "what time is it" in voice_data:
        alina_speak(time.ctime())
    if "search" in voice_data:
        search = record_audio("What do you want to search for?")
        url = f"https://www.google.com/search?q={search}"
        webbrowser.get().open(url)
        alina_speak(f"Here is what I found for {search}")
    if "find location" in voice_data:
        location = record_audio("What is the location?")
        url = f"https://google.nl/maps/place/{location}/&amp;"
        webbrowser.get().open(url)
        alina_speak(f"Here is the location of {location}.")
    if "toss a coin" in voice_data:
        coin_flip_with_random = "Heads" if random.random() > 0.5 else "Tails"
        alina_speak(f"You got {coin_flip_with_random}!")
    if "exit" in voice_data:
        alina_speak("Goodbye!")
        exit()
    if "tell a joke" in voice_data:
        joke = pyjokes.get_joke(language="en", category="neutral")
        alina_speak(joke)


if __name__ == "__main__":
    # Delay for one second
    time.sleep(1)
    alina_speak("How can I help you?")
    while True:
        voice_data = record_audio()
        respond(voice_data)
