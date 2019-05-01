import cv2
import numpy as np
import matplotlib.pyplot as plt
import math


def calc_contour(m_cx, m_cy):
    contour = []
    for angle_deg in range(0, 360):
        for pt in Rtable[angle_deg]:
            vec = [pt[0]*np.sin(pt[1]), pt[0]*np.cos(pt[1])]
            contour.append([[int(round(vec[0] + m_cy)), int(round(vec[1] + m_cx))]])

    return contour


I = cv2.imread("trybik.jpg")
IG = cv2.imread("trybik.jpg", cv2.IMREAD_GRAYSCALE)
ret, thresh1 = cv2.threshold(IG, 150,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours = contours[1:]

# # Finding main contour
# max_leng = -1
# it = -1
# for i, contour in enumerate(contours):
#     leng = len(contour)
#     it = i if leng > max_leng else it
#     max_leng = leng if leng > max_leng else max_leng
# print(max_leng)
# print(it)

# print(xy)


moments = cv2.moments(contours[3],  1)
centerr = [int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])]
print(centerr)
sobelx = cv2.Sobel(thresh1, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(thresh1, cv2.CV_64F, 0, 1, ksize=5)
grad = np.sqrt(sobelx**2 + sobely**2)
max_val = np.max(grad)
grad /= max_val
orient = np.arctan2(sobely, sobelx)
Rtable = [[] for i in range(360)]


for contour in contours:
    for it, pt in enumerate(contour):
        pt = pt[0]
        # Wektor łączący punkt konturu z punktem referencyjnym
        vec = pt - centerr
        # Euklidesowa odleglosc
        len = np.linalg.norm(vec)
        angle = np.arctan2(vec[1], vec[0])

        p1 = np.uint8(pt[0])
        p2 = np.uint8(pt[1])

        if 0 < p1 < 157 and 0 < p2 < 149:
            angle_deg = int(orient[p1, p2]*180/math.pi + 180)
        else:
            print(p1, p2)
        if angle_deg == 360:
            angle_deg = 0
        # print(angle_deg)
        Rtable[angle_deg].append([len, angle])
print(Rtable)

# cv2.drawContours(I, contours, 3, (255, 0, 0), 1)
# plt.figure(2)
# plt.imshow(I)
# plt.show()

#
# plt.figure(11)
# plt.imshow(I)
# plt.figure(1)
# plt.gray()
# plt.imshow(IG)
# plt.figure(2)
# plt.imshow(thresh1)
# plt.figure(3)
# plt.imshow(sobelx)
# plt.figure(4)
# plt.imshow(sobely)
# plt.figure(5)
# plt.imshow(grad)
# plt.figure(6)
# plt.imshow(orient)
# plt.show()
#

I2 = cv2.imread("trybiki2.jpg")
IG2 = cv2.imread("trybiki2.jpg", cv2.IMREAD_GRAYSCALE)
print(I2.shape[0], I2.shape[1])

ret2, thresh2 = cv2.threshold(IG2, 150,255,cv2.THRESH_BINARY)
sobel2x = cv2.Sobel(thresh2, cv2.CV_64F, 1, 0, ksize=5)
sobel2y = cv2.Sobel(thresh2, cv2.CV_64F, 0, 1, ksize=5)
grad2 = np.sqrt(sobel2x**2 + sobel2y**2)
max_val2 = np.max(grad2)
grad2 /= max_val2
orient2 = np.arctan2(sobel2y, sobel2x)

ak = np.zeros((2*I2.shape[0], 2*I2.shape[1]))
for x in range(grad2.shape[0]):
    for y in range(grad2.shape[1]):
        if grad2[x, y] > 0.5:
            angle_deg2 = int(orient2[x, y] * 180 / math.pi + 180)
            # print(angle_deg)
            if angle_deg2 == 360:
                angle_deg2 = 0
            for pt in Rtable[angle_deg2]:
                r = pt[0]
                fi = pt[1]
                # print(r)
                # print(fi)
                x1 = int(round(-r*np.cos(fi) + x))
                y1 = int(round(-r * np.sin(fi) + y))
                ak[y1, x1] += 1

plt.figure(1)
colors = ['r', 'g', 'b', 'y']
dt = 5
for j in range(0, 3):
    center = np.unravel_index(ak.argmax(), ak.shape)
    for x in range(-dt, dt):
        for y in range(-dt, dt):
            ak[center[0]+x, center[1] + y] = 0

    # cv2.circle(I2, center, 1, (0, 255, 0), thickness=3)
    plt.plot(center[0], center[1], '*', color=colors[j%4])
    cv2.drawContours(I2, np.array(calc_contour(center[1], center[0])), -1, (255, 0, 0), 1)

plt.imshow(I2)
plt.show()

