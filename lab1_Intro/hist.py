import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread('mandril.jpg')
IG = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
IGE = cv2.equalizeHist(IG)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
I_CLAHE = clahe.apply(IG)

cv2.imshow("Mandril",IG)
cv2.waitKey(0)
cv2.imshow("Mandril_IG",IGE)
cv2.waitKey(0)
cv2.imshow("Mandril_I_CLAHE",I_CLAHE)
cv2.waitKey(0)
cv2.destroyAllWindows()

# hist_opencv = cv2.calcHist([IG],[0],None,[256],[0,256])
#
#
# def hist(img):
#     h = np.zeros((256,1), np.float32) # tworzy i zeruje tablice jednokolumnowa
#     height, width = img.shape[:2] # shape - krotka z wymiarami - bierzemy 2 pierwsze
#     for y in range(height):
#         for x in range(width):
#             index = img[y][x]
#             h[index] += 1
#     return h
#
# my_hist = hist(IG)
#
# # print(hist_opencv)
#
# plt.figure(1)
# x = plt.hist(IG)
# print(x)
# plt.title('Histogram')
# plt.show()
