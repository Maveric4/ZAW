import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread("I.jpg")
J = cv2.imread("J.jpg")

IG = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
JG = cv2.cvtColor(J, cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(IG, JG)

# cv2.imshow("diff", diff)
# cv2.waitKey(0)

height = diff.shape[0]
width = diff.shape[1]

W2 = 1
dX = dY = 1

u = np.zeros(IG.shape, np.int8)
v = np.zeros(IG.shape, np.int8)


for j in range(0+W2+1, height-W2-1):
    for i in range(0+W2+1, width-W2-1):
        IO = np.float32(IG[j-W2 : j+W2+1, i-W2 : i+W2+1])
        min_sq_diff_sum = 10e9
        for y in range(-dX, dX + 1):
            for x in range(-dY, dY + 1):
                JO = np.float32(JG[j-W2+y : j+W2+1+y, i-W2+x : i+W2+1+x])
                sq_diff_sum = np.sum(np.sqrt((np.square(JO-IO))))
                if sq_diff_sum < min_sq_diff_sum:
                    min_sq_diff_sum = sq_diff_sum
                    x_min = y
                    y_min = x
        u[j, i] = x_min
        v[j, i] = y_min

plt.figure(1)
plt.gca().invert_yaxis()
# plt.imshow(IG)
plt.quiver(u, v)
plt.show()