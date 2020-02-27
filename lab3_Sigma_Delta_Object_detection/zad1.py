import numpy as np
k = np.ndarray(shape=(2,2), dtype=float, order='F')
k[:] = [[1,2],[3,4]]
c = np.ndarray(shape=(2,2), dtype=float, order='F')
c[:] = [[4,1],[1,2]]
print(k)
print(c)

print(k > c)

print(k.shape[1])