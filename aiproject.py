import speech_recognition as sr
import PyPDF2
import pyttsx3
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    try:
        print("Text: "+r.recognize_google(audio_text))
        s=r.recognize_google(audio_text)
    except:
         print("Sorry, I did not get that")
speak = pyttsx3.init()
speak.say(s)
speak.runAndWait()
