import pyttsx3 as pt
import speech_recognition as sr
from selinium_web import *  # type: ignore 

engine = pt.init()
rate=engine.getProperty('rate')
engine.setProperty('rate', 195)
                


voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
'''print(voices)
print(rate)'''
def speak(text):
    engine.say(text)
    engine.runAndWait() 

r = sr.Recognizer()

speak("hello!! i am kayal, your voice assistant! how are you? ")
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text) 

if "what" and "about" and "you" in text:
    speak("i am having a good day")
elif "dumbass" and "idiot" in text:
    speak("oh dear you are mean!!")
elif "sweetheart" and "darling" in text:
    speak("aww you are too sweet")
speak("what can i do for you?")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Go on :))")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    print(text2) 
 
if 'information' in text2:
    speak( "You need information on which topic, human")
    
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Okayy")
        audio = r.listen(source)
        infor1 = r.recognize_google(audio)
        print(infor1) 
        

    assist = info()   # type: ignore
    assist.get_info(infor1) 
