# to send whatsapp sms any time using python coding

from click import open_file
import requests 
import sys
import webbrowser
import bs4
import pywhatkit
import subprocess
res =requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text, "html.parser")
linkElement=soup.select('.r a')
linkToOpen=min(1,len(linkElement))
for i in range(linkToOpen):
command=input("type: ")
print(webbrowser.open('https://www.google.com/search?q='+command))
pywhatkit.sendwhatmsg('+91xxxxxxx918', "My demo program ignore it ",15  ,51) # send sms on whstapp
file=subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe')