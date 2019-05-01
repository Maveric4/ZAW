import cv2
import numpy as np
import matplotlib.pyplot as plt


def of(IG, JG, u0, v0, W2=1, dY=1, dX=1):
    height = IG.shape[0]
    width = IG.shape[1]
    u = np.zeros(IG.shape, np.int8)
    v = np.zeros(IG.shape, np.int8)
    for j in range(0 + W2 + 1, height - W2 - 1):
        for i in range(0 + W2 + 1, width - W2 - 1):
            # print(u0[j, i])
            IO = np.float32(IG[j - W2: j + W2 + 1, i - W2: i + W2 + 1])
            min_sq_diff_sum = 10e9
            for y in range(-dX, dX + 1):
                for x in range(-dY, dY + 1):
                    JO = np.float32(JG[j - W2 + y + u0[j, i]: j + W2 + 1 + y + u0[j, i], i - W2 + x + v0[j, i] : i + W2 + 1 + x + v0[j, i]])
                    sq_diff_sum = np.sum(np.sqrt((np.square(JO - IO))))
                    if sq_diff_sum < min_sq_diff_sum:
                        min_sq_diff_sum = sq_diff_sum
                        x_min = y
                        y_min = x
            u[j, i] = x_min + u0[j, i]
            v[j, i] = y_min + v0[j, i]
    return u, v


def pyramid(im, max_scale):
    images = [im]
    for k in range(1, max_scale):
        images.append(cv2.resize(images[k-1], (0, 0), fx=0.5, fy=0.5))
    return images


I = cv2.imread("I.jpg")
J = cv2.imread("J.jpg")

IG = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
JG = cv2.cvtColor(J, cv2.COLOR_BGR2GRAY)

max_scale = 3
IP = pyramid(IG, max_scale)
JP = pyramid(JG, max_scale)

u0 = np.zeros(IP[-1].shape, np.uint8)
v0 = np.zeros(JP[-1].shape, np.uint8)

for k in range(1, max_scale+1):
    if k != 1:
        u0 = cv2.resize(u, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
        v0 = cv2.resize(v, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
    u, v = of(IP[-k], JP[-k], u0, v0)

plt.figure(1)
plt.gca().invert_yaxis()
# plt.imshow(IG)
plt.quiver(u, v)
plt.show()