import numpy as np

a=np.array(range(1,17))
a.shape=(4,4)               # it will return elements in 4*4 order having elements 1 to 16
print(a)
print(a.flatten())              # change any array in 1-D array
print(np.ravel(a))                     # change any array in 1-D array

b=np.array(range(1,17))
a.reshape(2,4,2)               # it will return elements in 4*4 order having elements 1 to 16
print(a)