import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()    
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)     #to change the voice into male ou female

def talk(text):
    engine.say(text)
    engine.runAndWait() 


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            talk('I am listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Anurag' in command:
                command = command.replace('Anurag','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing...' + song)
        pywhatkit.playonyt(song)                          # play any thing on youtube
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p') #use %S to show time in seconds
        talk('Current time is ' + time)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 20)      # pass the number of lines in which you need to get answer
        print(info) 
        talk(info)
    elif 'date' in command:
        talk('Sorry,I have a headache. and My mother will also not allow me to do all this.')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi and your coding. Directly saying I am not interested.sister ') 
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'who are you' in command:
        talk('I am persnal assistant of Mr. Anurag Singh Chauhan.Developed by him in 0ctober two thousand twenty two')
        print('I am persnal assistant of Mr. Anurag Singh Chauhan.Developed by him in 0ctober 2022')

    else:
        talk('Please say the again.You are not clearly audible')
        print("Please say the again.You are not clearly audible")
    
while True:
    run_alexa()