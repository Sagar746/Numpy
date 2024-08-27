import numpy as np


arr1 = np.array([1,2,5,6,7])

arr2 = np.array([5,6,7,8,9])

result = np.union1d(arr1, arr2)
print(result)




# ------------------------------------

'''
If we want to find union of more than two arrays, then we can 
find that by using functools.reduce function
'''

from functools import reduce

arr1 = np.array([[1,2,3], [4,5,6],[10,11,12]])

arr2 = np.array([[0,5,1], [7,8,9],[11,13,14]])


result = reduce(np.union1d, (arr1,arr2))
print(result)