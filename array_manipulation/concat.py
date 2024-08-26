import numpy as np

'''
concat method can combine dataframes along with either rows and columns.
'''

arr1 = np.array([1,2])
arr2 = np.array([3,4])


array_new = np.concatenate((arr1, arr2))
print(array_new)


# ---------------------------------------------

    # ENUMERATE NUMPY ARRAY

arr = np.arange(5)
arr1 = np.arange(10).reshape(2,5)

for a,b in np.nditer([arr, arr1]):
    print(f'{a} : {b}')