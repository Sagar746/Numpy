import numpy as np

'''
split(), array_split()
'''


array = np.arange(6)

result = np.array_split(array,2)
print(result)