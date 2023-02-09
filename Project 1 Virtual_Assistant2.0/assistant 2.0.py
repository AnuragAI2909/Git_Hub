import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser 
import subprocess
import calendar 


listener = sr.Recognizer()    
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)              #to change the voice into male ou female 


def talk(text):
    engine.say(text)
    engine.runAndWait() 


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            talk('Sir,I am listening')
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
    if 'play' in command:
        song = command.replace('anu play', '')
        talk('Playing...' + song) 
        pywhatkit.playonyt(song)                               # play any thing on youtube


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p') #use %S to show time in seconds
        talk('Current time is ' + time)


    elif 'tell me about' in command:
        talk('wait i am search...')
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 10)                     # pass the number of lines in which you need to get answer
        print(info) 
        talk(info)


    elif 'date' in command:
        talk(' Sorry, I have a headache. and My mother will also not allow me to do all this.')


    elif 'are you single' in command:
        talk('I am in a relationship with wifi.') 


    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())


    elif 'who are you' in command:
        talk('I am persnal assistant of Mr. Anurag Singh Chauhan. Developed by him in october two thousand twenty two')
        print('I am persnal assistant of Mr. Anurag Singh Chauhan. Developed by him in 0ctober 2022')



    elif 'your name'in command:
        talk("I am your persnal assistant, You can call me Anu.")



    elif 'calendar' in command:
        talk("Sir i'm printing the calendar of 2022, because i'm  unable to recognise you, if you want to print calendar of any other year, it will be easy for me if you enter the year" )
        print(calendar.calendar(2022))
        command=int(input("Year name : "))
        print()
        talk("printing calendar" )
        print(calendar.calendar(command))


    elif 'what is' in command:
        talk('i am searching for it, please wait ')
        command=command.replace('what is ','')
        webbrowser.open('https://www.google.com/search?q='+command)
       

    elif  'start writing' in command:
        talk(' opening please wait a while')
        command=command.replace('open file','')
        command=command.replace('and write','')
        a=open('D:\\hp\\Documents\\ann.txt','a') 
        a.write(command)
        a.close()


    elif 'open chrome' in command:
        talk('chrome is opening please wait a while')
        file=subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe')
    

    else:
        talk('Please say the again.')
       
while True:
    run_anurag()