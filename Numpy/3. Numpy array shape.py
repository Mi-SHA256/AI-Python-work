import numpy as np
import pandas as pd

array2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
shape = array2.shape
print("Shape: ", shape) #tells structure of shape

reshaped = array2.reshape(-1) #take 1 dimension away to make it 1D
print("Reshape:", reshaped)