def fact(num):
    f=1
    while(num>0):
      f=f*num
      num-=1
    print("Factorial of the number is :",f)
def fab(num1):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(0,num1-2):
        c=a+b
        print(c)
        a=b
        b=c
num1=int(input("Enter the number of term up to which you want to print series : "))
fab(num1)
num=int(input("Enter the number for factorial:  "))
fact(num)

