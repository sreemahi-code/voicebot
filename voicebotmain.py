import pyttsx3 as pt
import speech_recognition as sr
engine = pt.init()
rate=engine.getProperty('rate')
engine.setProperty('rate', 200)

voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
'''print(voices)
print(rate)'''
def speak(text):
    engine.say(text)
    engine.runAndWait() 

r = sr.Recognizer()

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text) 
