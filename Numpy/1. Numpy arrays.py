import pandas as pd
import numpy as np

a =  np.array([10,20,30,40,50])

b = np.array([[1,2,3], [4,5,6], [7,8,9]])

c = np.array([[[1,2], [4,5] ,[7,8]]], dtype="int64") #dtype 32 is default

print(a.ndim) #dimensions
print(b.ndim)
print(c.ndim)
print("")
print(a.shape)
print(b.shape)
print(c.shape) #shape of array
print("")
print(a.dtype)
print(b.dtype)
print(c.dtype)
print("")
print(a.itemsize) #number of bytes
print(b.itemsize) #dtype affects size of bytes 16 = 2, 32 = 4, 64 = 8
print(c.itemsize)
print("")
print(a.nbytes) #total size of elements
print(b.nbytes)
print(c.nbytes)