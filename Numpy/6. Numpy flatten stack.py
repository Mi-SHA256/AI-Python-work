import numpy as np
import pandas as pd

#flatten stack with np

array2 = np.array([[1,2,3],[4,5,6]])

print("Flattened array: ",array2.flatten())

array22 = np.array([[7,8,9],[10,11,12]])

verstack = np.vstack((array2, array22))
print("Ver Stacked arrays: ", verstack)

Hstack = np.hstack((array2, array22))
print("Hrz Stacked arrays: ", Hstack)