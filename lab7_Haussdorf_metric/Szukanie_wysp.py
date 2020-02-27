import cv2
import numpy as np
import matplotlib.pyplot as plt
import copy
import os


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

    # x /= (x_max-x_min)
    # y /= (y_max-y_min)
    for i in range(x.shape[0]):
        x[i] /= (x_max-x_min)
    for i in range(y.shape[0]):
        y[i] /= (y_max-y_min)

    return x, y, center


def euk_len(xA, yA, xB, yB):
    return np.sqrt((xA-xB)**2 + (yA-yB)**2)


def calc_dH_side(xA, yA, xB, yB):

    min = np.ones(xA.shape[0])*1e10
    for it in range(xA.shape[0]):
        for i in range(xB.shape[0]):
            len = euk_len(xA[it], yA[it], xB[i], yB[i])
            min[it] = len if len < min[it] else min[it]
    max_len = np.max(min)
    return max_len


def calc_dH(xA, yA, xB, yB):
    return max(calc_dH_side(xA, yA, xB, yB),calc_dH_side(xB, yB, xA, yA))

mapa_kolor = I = cv2.imread('Aegeansea.jpg')
I_HSV = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)

IG_temp1 = I_HSV[:, :, 1]
IG_temp1[IG_temp1 >= 30] = 255
IG_temp1[IG_temp1 < 30] = 0

IG_temp2 = I_HSV[:, :, 0]
IG_temp2[IG_temp2 >= 60] = 255
IG_temp2[IG_temp2 < 60] = 0
IG_temp2 = cv2.bitwise_not(IG_temp2)
IGN = IG_temp1 * IG_temp2

contours_all = cv2.findContours(IGN, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0]
contours_all = [el for el in contours_all if 3000 > el.shape[0] > 15]

listdir = os.listdir('imgs/')
lengths = dict()
i = 0
for image in listdir:
    IGN = cv2.bitwise_not(cv2.imread('imgs/' + image, cv2.IMREAD_GRAYSCALE))
    contours = cv2.findContours(IGN, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0]
    xA, yA, centerA = normalizeContour(contours[0])

    dict_idx = dict()
    dict_centers = dict()
    for idx, contour in enumerate(contours_all):
        # print(idx)
        xB, yB, centerB = normalizeContour(contour)
        max_len = calc_dH(xA, yA, xB, yB)
        dict_idx[idx] = max_len
        dict_centers[idx] = centerB

    found_contour_idx = min(dict_idx, key=dict_idx.get)

    cv2.putText(mapa_kolor, image.split('.')[0].split('_')[1], (int(dict_centers[found_contour_idx][0]), int(dict_centers[found_contour_idx][1])),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
    print(image)
    i += 1
    if i == 5:
        break

plt.figure(1)
plt.imshow(mapa_kolor)
plt.show()
plt.savefig('wyspy.png')



