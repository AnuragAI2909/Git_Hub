class Circle:
    'Using constructor'
    def __init__(self,r1=10):
        self.r1=r1
    def get(self):
        print("radius = ",self.r1)
    def Area(self):
        ar=3.14*(self.r1)*(self.r1)
        print("Area of the circle= ",ar)

s=Circle()
r=float(input("Enter the size of radius: "))
s.__init__(r)
s.get()
s.Area() 

