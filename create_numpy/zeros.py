import numpy as np
# np.zeros(shape, dtype, order)

x = np.zeros([4,3],dtype=[('x','float'), ('y','int')], order='C')
print(x)


# -------------------------


y = np.zeros([4,3], dtype=int, order='C')
print(y)