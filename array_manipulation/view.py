import numpy as np


'''
view() has the same memory location as the original array( Shallow Copy)

when we make changes to the view it affects the original array, 
and when we make changes to the original array it affects the view
'''



arr = np.array([1,2,3,4,5])

v = arr.view()
print(f'id of arr : {id(arr)}')
print(f'id of v: {id(v)}')

arr[0] = 12

print(f'Original array: {arr}')
print(f'view -v : {v}')
