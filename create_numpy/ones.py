import numpy as np
'''
 np.ones(shape, dtype, order)
'''

x = np.ones([4,3])
print(x)

# --------------------------------------------

y = np.ones([2,2], dtype=int, order='F')

print(y)


# flatten() a matrix into one dimension array

flat = x.flatten()
print(flat)