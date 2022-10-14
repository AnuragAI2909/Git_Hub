import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import subprocess


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

def run_anurag():
    command = take_command()
    if 'anu play' in command:
        song = command.replace('anu play', '')
        talk('Playing...' + song) 
        pywhatkit.playonyt(song)                          # play any thing on youtube

    elif ('anu time' or 'anurag time') in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p') #use %S to show time in seconds
        talk('Current time is ' + time)

    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 10)      # pass the number of lines in which you need to get answer
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

    elif 'your name'in command:
        talk("My name is Anurag, You can call me Anu. I'm  powered by  python coding.")
    
    elif 'what is' in command:
        
        webbrowser.open('https://www.google.com/search?q='+command)

    elif 'open chrome' in command:
        talk('chrome is opening please wait a while')
        file=subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe')


    elif 'open file' and 'and write' in command:
        talk(' opening please wait a while')
        command=command.replace('open file','')
        command=command.replace('and write','')
        a=open('D:\\hp\\Documents\\ann.txt','a') 
        a.write(command)
        a.close()
        file=subprocess.Popen('D:\\hp\\Documents\\ann.txt')


    else:
        talk('Please say the again.You are not clearly audible')
       
    
while True:
    run_anurag()