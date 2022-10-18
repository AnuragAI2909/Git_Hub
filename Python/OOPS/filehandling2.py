from collections import Counter
a=open("C:\\Users\\hp\\Desktop\\OS\\f1.txt",'r+')
a1=a.read()
print("Content of file f1:\n",a1,)
a.seek(0)
a2=len(a.readlines())
print("Number of lines in f1 file =",a2,"\n\n") 

b=open("C:\\Users\\hp\\Desktop\\OS\\f2.txt",'r+')
b1=b.read()
print("Content of file f2:\n",b1)
b.seek(0)
b2=len(b.readlines()) 
print("Number of lines in f2 file =",b2,"\n\n")
 
d=open("C:\\Users\\hp\\Desktop\\OS\\f3.txt",'a')
d.write(a1+"\n")
d.write(b1)

a.seek(0) 
a3=a.read().split()
c=Counter(a3)
a.seek(0)
n=c.most_common(1)
print("Occurance of word in f1:",n) 


a.seek(0) 
b3=b.read().split()
c1=Counter(b3)
b.seek(0)
n1=c1.most_common(1)
print("Occurance of word in f2:",n1)   

a.close()
b.close()
d.close()