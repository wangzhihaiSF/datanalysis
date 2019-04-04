import numpy as np
# 连续数组创建
x = np.arange(1, 11, 2)
y = np.linspace(1, 9, 5)

print(x)
print(y)
print(np.add(x, y))
print(np.subtract(x, y))
print(np.multiply(x, y))
print(np.divide(x, y))
print(np.power(x, y))