import numpy as np


an_array = np.array([[1,2], [3,4]])

another_array = np.array([[1,2], [3,4]])

comparision = an_array == another_array
print(comparision.all())

# ----------------------------------------------

if np.array_equal(an_array, another_array):
    print('Equal')
else:
    print('Not Equal')

