# some operations of file handling ... 
a=open('C:\\Users\\hp\\Desktop\\OS\\SW3.docx','w')
a.write("Hellow anurag singh chauhan")
print(a.tell())
a.seek()
a.writelines(["anu ","ai","btech"])    
a.close()
print(a.closed) 
a=open('D:\Coding\Python\Test1.py','a')
print(a.tell())
a.seek(0) 
a.write("Hello")
a.close()      
a=open("D:\Coding\Python\download.jpg","rb")
b=open("D:\Coding\Python\download2.jpg","wb")
b.write(a.read())
a.close()
b.close()                                                                                    