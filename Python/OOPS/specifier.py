# working of protected and private variables 
class Anurag:
    nm="Anurag"
    _bt=2025
    __age=18
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
print(anu1.mob)
print(anu1._bt)                             # calling protected variable usimg object of child class
print(anu._Anurag__age)                    # method of calling private varialble (object._Anurag__)
print(type(anu._Anurag__age))
print(anu1.__age)                         #it will show error bcz __age is private it cant clled usimg pbject of child clASS

