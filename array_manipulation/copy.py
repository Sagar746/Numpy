import numpy as np


'''
copy() is the new array which is physically stored at another memory location(Deep Copy)

'''




arr = np.array([1,2,3,4,5])

c = arr.copy()
print(f'id of arr: {id(arr)}')
print(f'id of copy: {id(c)}')

arr[0]=12
print(f'original array: {arr}')
print(f'copy -: {c}')