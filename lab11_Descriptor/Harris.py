#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage.filters as filters


def find_max(image, size, threshold) : # size - rozmiar maski filtramaksymalnego
    data_max = filters.maximum_filter(image, size)
    maxima = (image == data_max)
    diff = image > threshold
    maxima[diff == 0] = 0
    return np.nonzero(maxima)


def calcH(imgG, size):
    k = 0.05
    sobelx = cv2.Sobel(imgG, cv2.CV_32F, 1, 0, ksize=size)
    sobelxx_bG = sobelx*sobelx
    sobelxx = cv2.GaussianBlur(sobelxx_bG,(size, size), 0)
    sobely = cv2.Sobel(imgG, cv2.CV_32F, 0, 1, ksize=size)
    sobelyy_bG = sobely*sobely
    sobelyy = cv2.GaussianBlur(sobelyy_bG,(size, size), 0)
    sobelxy_bG = sobelx*sobely
    sobelxy = cv2.GaussianBlur(sobelxy_bG,(size, size), 0)

    detM = sobelxx * sobelyy - sobelxy**2
    traceM = sobelxx + sobelyy
    H = detM - k*traceM**2
    return H/H.max()


def draw_max(img, coord):
    plt.figure()
    plt.imshow(img)
    plt.plot(coord[1], coord[0], '*', color='r')


# img2 = cv2.imread('fontanna2.jpg')
# img1 = cv2.imread('fontanna1.jpg')
# img1 = cv2.imread('budynek1.jpg')
# img2 = cv2.imread('budynek2.jpg')
img1 = cv2.imread('fontanna1.jpg')
img2 = cv2.imread('fontanna2.jpg')

img1G = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2G = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# ksize = 7
ksize = 3
threshold = 0.2
img1_H = calcH(img1G, ksize)
img2_H = calcH(img2G, ksize)

max_img1 = find_max(img1_H, ksize, threshold)
max_img2 = find_max(img2_H, ksize, threshold)

draw_max(img1, max_img1)
draw_max(img2, max_img2)
plt.show()











