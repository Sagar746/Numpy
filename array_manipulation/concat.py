import numpy as np

'''
concat method can combine dataframes along with either rows and columns.
'''

arr1 = np.array([1,2])
arr2 = np.array([3,4])


array_new = np.concatenate((arr1, arr2))
print(array_new)