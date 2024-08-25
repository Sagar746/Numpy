import numpy as np


arr1 = np.array([[1,2,3],[11,12,13]])

arr2 = np.array([[4,5,6],[7,8,9]])

h_append = np.vstack((arr1,arr2))
print(h_append)