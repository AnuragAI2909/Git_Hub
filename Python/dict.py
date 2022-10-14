# some function of dictionary 
a={
    "Name":"Anurag",
    "Batch": "2021"
}
print(a)
s=input("enter key:")
y=a.keys()
for i in y:
    if(i==s):
        print("ok")
        exit()

print("Not found")    
print(p:=a.get("a","False"))  # if key a is present then it will printa otherwise false 