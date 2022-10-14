# to print text of any website 
import requests
r=requests.get("https://www.w3schools.com/ai/default.asp")
print(r.text)
