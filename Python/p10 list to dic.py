lst=[("Anurag",2),("Sargam",4),("Ammar",5),("Acand",6)]
print("Given list of tuple: ")
print(lst)
dic1=dict()
for stdu,enroll in lst:
    dic1.setdefault(stdu,[]).append(enroll)
print("Output", dic1)