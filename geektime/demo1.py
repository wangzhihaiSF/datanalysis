import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1, 1] = 10
c = np.array([(1, 4, 8), (2, 6, 90)])
print(a.shape)
print(b.shape)
print(a.dtype)
print(b, "###########")
print(c)