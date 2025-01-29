import numpy as np

'''
    np.linspace(start, stop, num)
'''

x, step = np.linspace(2,10, num=5, retstep=True)
print(x, '\n')
print(step)
# -----------------------------

y = np.eye(2,4) 
print(y)
