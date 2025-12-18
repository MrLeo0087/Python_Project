from gtts import gTTS
import speech_recognition as sr
import playsound
import random
import os
import pandas as pd
import pyttsx3 as ts
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import socket

model = Model("vosk-model-small-en-in-0.4") 
recognizer = KaldiRecognizer(model, 16000)

def internet_status(timeout=3):
    try:
        socket.create_connection(("8.8.8.8",53),timeout==timeout)
        return True
    
    except OSError:
        return False
    


if not os.path.exists('data.csv'):

    data = {
        'Roll Number':['1','2','3','4','5','6','7','8'],
        "Name":['Darshan','Sunita','Prakash','Nishant','Rahul','Gita','Manisha','Rohit'],
        "Attandance" : [0,0,0,0,0,0,0,0]

    }
    df = pd.DataFrame(data)
    df.to_csv('data.csv',index=False)

def speak_online(text):
    print("Mam : ", text)
    try:
        tts = gTTS(text=text, lang='en')
        filename = f"voice_{random.randint(1,10000)}.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("Error:", e)
        
def speak_offline(audio):
    print("Mam : ",audio)
    engine = ts.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)   
    engine.setProperty('rate', 180)            
    engine.setProperty('volume', 1.0)            

    engine.say(audio)
    engine.runAndWait()

def takecommand_online(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening.....")
        r.pause_threshold = 1
        r.energy_threshold = 100
        try:
            audio = r.listen(source, timeout=7, phrase_time_limit=4)

        except sr.WaitTimeoutError:
            return None

    try:
        print("Recognition ....\n ")
        query = r.recognize_google(audio, language='en-in')
        print(f"Student : {query}")
    except Exception as e:
        print("Listening .....")
        return None
    return query



def takecommand_offline():
    print("Listening (offline)...")

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype='int16',
        channels=1
    ) as stream:
        while True:
            data, _ = stream.read(4000)
            if recognizer.AcceptWaveform(bytes(data)):
                result = recognizer.Result()
                text = json.loads(result).get("text", "")
                print(f"Student: {text}")
                return text.lower().strip()

def takecommand():
    if internet_status():
        return takecommand_online()

    else:
        return takecommand_offline()

def speak(name):
    if internet_status():
        speak_online(name)
        
    else:
        speak_offline(name)

# text = takecommand()
# speak(text)

choose = input("Enter a for attandance : ")
if choose =='a':
    speak("Hello everyone, Let's take attandance .. Listen carefully ! ")
    df = pd.read_csv("data.csv")

    for name in df["Name"]:
        speak(name)
        text = takecommand()
        if text:
            text = text.lower().strip()


        if text == "present" or text=='yes' or text == 'yes mam' or text == "present mam":
            df.loc[df["Name"] == name, "Attandance"] += 1
            df.to_csv("data.csv", index=False)
            from mam_respond import mam_respond_present
            resp = mam_respond_present()
            speak(resp)

        elif text == "absent" or text=='not present' or text == None:
            from mam_respond import mam_respond_absent
            resp = mam_respond_absent()
            speak(resp)

        elif text !="present" and text!='absent':
            speak("I can't understand, Say again !") 
            retext = takecommand()

            if retext:
                retext = retext.lower().strip()

            if retext == "present":
                df.loc[df["Name"] == name, "Attandance"] += 1
                df.to_csv("data.csv", index=False)
                from mam_respond import mam_respond_present
                resp = mam_respond_present()
                speak(resp)

            elif retext == "absent":
                speak("Marked absent")
    speak("Thank you everyone, Have a nice day !")