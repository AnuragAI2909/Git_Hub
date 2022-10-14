import collections as c
a=[1,2,3,4,5,6,7,8,9,2,6,3,2]
print(c.Counter(a))
print(c.Counter(a).most_common(1)) #return most occured number and its no. of occurence

