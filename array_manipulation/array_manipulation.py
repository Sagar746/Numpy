import numpy as np

arr = np.array([1,2,3,4,5])

# append at the end of the array
ap = np.append(arr, [6,7,8,9])
print(ap)


# -----------------------------------------------------------

arr = np.arange(1,13).reshape(2,6)

print(f'array to be appended columnwise')
col = np.arange(5,11).reshape(1,6)
print(col)

print(f'array after appending column-wise')
arr_col = np.append(arr,col, axis=0)
print(arr_col) 


# -------------- SWAPPING THE COLUMN OF ARRAY --------------

print(arr)
print('\n')    #new line

arr[:, [0,2]] = arr[:, [2,0]]
print(arr)


# -------------------------------------------------------------
