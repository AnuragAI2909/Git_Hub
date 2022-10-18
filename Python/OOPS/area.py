class Circle:
    
    def get(self,r):
        print("radius = ",r)
    def Area(self,r):
        ar=3.14*r*r
        print("Area of the circle= ",ar)

s=Circle()
r=float(input("Enter the size of radius: "))
s.get(r)
s.Area(r) 