import numpy as np


x = np.array([[1,2], [4,5]])
y = np.array([[7,8], [9,10]])

add1 = np.add(x,y)
print(add1)

sub = np.subtract(x,y)
print(sub)

div = np.divide(x,y)
print(div)

mul = np.multiply(x,y)
print(mul)

dot = np.dot(x,y)
print(dot)

# tranpose of matrix

print(x.T)



# ---------------------------

arr1 = np.identity(3)
print(arr1)

