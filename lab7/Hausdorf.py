import cv2
import numpy as np
import matplotlib.pyplot as plt
import copy
import os

# IG = cv2.imread("imgs/s_skiathos.bmp")
# IGN = cv2.bitwise_not(cv2.imread("imgs/s_skiathos.bmp", cv2.IMREAD_GRAYSCALE))

IG = cv2.imread("ithaca_q.bmp")
IGN = cv2.bitwise_not(cv2.imread("ithaca_q.bmp", cv2.IMREAD_GRAYSCALE))
# im2, contours, hierarchy\
x = cv2.findContours(IGN, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours = x[0]
hierarchy = x[1]
# print(contours)
# print(hierarchy)


def normalizeContour(contour):
    c = copy.deepcopy(contour)
    x = c[:, 0, 0]
    y = c[:, 0, 1]
    x = np.array(x, dtype=np.float64)
    y = np.array(y, dtype=np.float64)
    moments = cv2.moments(c,  1)
    center = [int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])]
    x -= center[0]
    y -= center[1]

    x_min = np.min(x)
    y_min = np.min(y)
    x_max = np.max(x)
    y_max = np.max(y)

    x /= (x_max-x_min)
    y /= (y_max-y_min)

    x_min = np.min(x)
    y_min = np.min(y)
    x_max = np.max(x)
    y_max = np.max(y)

    for i in range(x.shape[0]):
        x[i] /= (x_max-x_min)
    for i in range(y.shape[0]):
        y[i] /= (y_max-y_min)
    print(x_min, y_min, x_max, y_max)

    len_max = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[0]):
            leng = euk_len_sq(x[i], y[i], x[j], y[j])
            len_max = leng if leng > len_max else len_max


    len_max = np.sqrt(len_max)
    for i in range(x.shape[0]):
        x[i] /= len_max #(x_max-x_min)
    for i in range(y.shape[0]):
        y[i] /= len_max #(y_max-y_min)

    x_min = np.min(x)
    y_min = np.min(y)
    x_max = np.max(x)
    y_max = np.max(y)
    print(x_min, y_min, x_max, y_max)
    print()


    return x, y, center


def euk_len_sq(xA, yA, xB, yB):
    return (xA-xB)**2 + (yA-yB)**2


def calc_dH_side(xA, yA, xB, yB):

    min = np.ones(xA.shape[0])*1e12
    for it in range(xA.shape[0]):
        for i in range(xB.shape[0]):
            len = euk_len_sq(xA[it], yA[it], xB[i], yB[i])
            min[it] = len if len < min[it] else min[it]
    max_len = np.max(min)
    return np.sqrt(max_len)


def calc_dH(xA, yA, xB, yB):
    return max(calc_dH_side(xA, yA, xB, yB),calc_dH_side(xB, yB, xA, yA))


xA, yA, centerA = normalizeContour(contours[0])

cv2.drawContours(IG, contours, -1, (255, 0, 0), 1)
IG[centerA[0], centerA[1]] = (0, 255, 0)
plt.figure(1)
plt.gray()
plt.imshow(IG)
plt.figure(2)
plt.imshow(IGN)
plt.show()

listdir = os.listdir('imgs/')
dict = dict()
for image in listdir:
    IGN = cv2.bitwise_not(cv2.imread('imgs/' + image, cv2.IMREAD_GRAYSCALE))
    contours = cv2.findContours(IGN, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0]
    xB, yB, centerB = normalizeContour(contours[0])
    # x_min = np.min(xB)
    # y_min = np.min(yB)
    # x_max = np.max(xB)
    # y_max = np.max(yB)
    # print(x_min,
    # y_min,
    # x_max,
    # y_max)
    max_len = calc_dH(xA, yA, xB, yB)
    dict[image] = max_len

image = min(dict, key=dict.get)
print(image)


# mapa_kolor = I = cv2.imread('Aegeansea.jpg')
# # IGN = cv2.imread('Aegeansea.jpg', cv2.IMREAD_GRAYSCALE)
# I_HSV = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
#
#
# IG_temp1 = I_HSV[:, :, 1]
# # truth1 = (IG_temp1 >= 30)*1
# IG_temp1[IG_temp1 >= 30] = 255
# IG_temp1[IG_temp1 < 30] = 0
# IG_temp2 = I_HSV[:, :, 0]
# IG_temp2[IG_temp2 >= 60] = 255
# IG_temp2[IG_temp2 < 60] = 0
# IG_temp2 = cv2.bitwise_not(IG_temp2)
# IGN = IG_temp1 * IG_temp2
#
# contours_all = cv2.findContours(IGN, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0]
# contours_all = [el for el in contours_all if 3000 > el.shape[0] > 15]
#
# plt.figure(2)
# cv2.drawContours(mapa_kolor, contours_all, -1, (255, 0, 0), 1)
# plt.imshow(mapa_kolor)
# plt.show()
# # for i in range(IG_temp1.shape[0]):
# #     for j in range(IG_temp1.shape[1]):
# #         IG_temp[i, j] = 0 if IG_temp[i, j]
#
# # print(IGN)
# # plt.figure(1)
# # plt.imshow(IG)
# # plt.figure(2)
# # plt.gray()
# # plt.imshow(IGN)
# # plt.show()
#
#
#
# IGN = cv2.bitwise_not(cv2.imread("imgs/c_astipalea.bmp", cv2.IMREAD_GRAYSCALE))
# cont_pattern = cv2.findContours(IGN, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0][0]
# xA, yA, centerA = normalizeContour(cont_pattern)
#
#
#
# dict_idx = dict()
# dict_centers = dict()
# for idx, contour in enumerate(contours_all):
#     # print(idx)
#     xB, yB, centerB = normalizeContour(contour)
#     max_len = calc_dH(xA, yA, xB, yB)
#     dict_idx[idx] = max_len
#     dict_centers[idx] = centerB
#     cv2.putText(mapa_kolor, str(idx), (int(centerB[0]), int(centerB[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
#
# print(dict_idx)
# found_contour_idx = min(dict_idx, key=dict_idx.get)
# print(found_contour_idx)
#
# cv2.putText(mapa_kolor, "FOUND", (int(dict_centers[found_contour_idx][0]), int(dict_centers[found_contour_idx][1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
#
# plt.figure(1)
# plt.imshow(mapa_kolor)
# plt.show()
#
#
