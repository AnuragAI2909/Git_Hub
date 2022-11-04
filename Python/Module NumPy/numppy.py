import numpy as np
a=np.array([1,2,3,4,5])
print(a.ndim)                       #return the dimention of array
print(a.shape)                      #return 5*1 in this or dimentions in cross type
print(a.dtype)                      #size of storage

b=np.array(1)                         # zero dimention
print(b.ndim)

c=np.array([[1,2],[3,4],[5,6]])
print(c.ndim)
print(c.shape)                            #2*3

d=np.array([[1,2,3],[4,5,6]])
print(d.ndim)           
print(d.shape)                            #3*2 size

e=np.array([[[1,2],[3,4]],[[4,5],[6,7]]])
print(e.ndim)
print(e.shape)
