a={
    'a':1,
    'b':2
}
a1={
    'c':3,
    'd':4
}
a2={
    'e':5,
    'f':6

}                         
a.update(a1)
a.update(a2)
print(a)
 
# or ⬇️

b={**a,**a1,**a2}
print(b)