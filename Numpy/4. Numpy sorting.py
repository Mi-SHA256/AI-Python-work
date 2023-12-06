import numpy as np
import pandas as pd

array1D = np.array([10,30,20,50,40])
sort = np.sort(array1D)

print("Sorted: ", sort)

min = array1D.min()
max = array1D.max()

print("Min value: ", min)
print("Max value: ", max)

indices = np.where(array1D > 30)
print("Indices >30: ",indices)