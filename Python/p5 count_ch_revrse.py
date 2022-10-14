def reverse_word(s):
    w=s.split()
    w.reverse()
    a=' '.join(w)
    print("Reversed string is:",a)
    
def count_char(s):
    f=0
    for element in s:
        f+=1
    print("Number of character in the string are: ",f)
s=input("ENter any string:")
reverse_word(s)
count_char(s)
