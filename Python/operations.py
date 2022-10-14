#calculator

n1=eval(input("Enter the first number :"))
n2=eval(input("Enter the second number :"))
ch=input("A-->SUM ,B-->SUBSTRACT ,C-->MULIPLY ,D-->DIVISION ") 
ch=input("Enter your choice")
if(ch=='A'):
    print("Addition:",(n1+n2))
elif(ch=='B'):
      print("Substraction:",(n1-n2))
elif(ch=='C'):
      print("Multiplication:",(n1*n2))
elif(ch=='D'):
      print("Division:",(n1/n2))
else:
    print("Wrong choice ...")

