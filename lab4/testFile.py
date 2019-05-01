import numpy as np
import matplotlib.pyplot as plt
# for i in range(1, 10):
#     print(i)

# u = np.matrix([[1, 2 , 3], [4, 5, 6],[7, 8, 9]])
# v = 2*u
u = np.zeros((3, 3), np.int8)
v = np.zeros((3, 3), np.int8)
i = 0
for x in range(u.shape[0]):
    for y in range(u.shape[1]):
        u[x, y] = i
        i+=2

for x in range(u.shape[0]):
    for y in range(u.shape[1]):
        v[x, y] = 0
        i+= 4
print(u)

plt.figure(1)
plt.gca().invert_yaxis()
# plt.imshow(IG)
plt.quiver(u, v)
plt.show()