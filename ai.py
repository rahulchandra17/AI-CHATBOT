from joblib import load
import speech_recognition as sr
import pyttsx3

conv = load('conversation')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=5)
    try:
        print('recognising...')
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)
        print('say that again please')
        return 'none'
    return query

if __name__ == '__main__':
    while True:
        query = takecommand().lower()
        speak(conv.predict([query]))