class Anurag:
    'This class is performing the working inheritance'
    nm="Anurag"
    bt=2025
    age=18     
    def Display(Self):
        print("hyyy")
class Anurag1(Anurag):
    mob=2252
    acc=3676
    def Display1(self):
        print("Hellow")

anu=Anurag()
anu1=Anurag1()
print(anu.nm)
print(anu1.nm)
print(Anurag.__doc__)                     
print(anu1.mob)
print(anu1.bt)   
print(anu.bt)                         
print(anu1.acc)                    
print(anu.age)
print(anu1.age)