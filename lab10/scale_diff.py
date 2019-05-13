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

def find_extr(image, size, threshold) : # size - rozmiar maski filtramaksymalnego
    data_max = filters.maximum_filter(image, size)
    data_min = filters.minimum_filter(image, size)
    extr = (image == data_max or data_min)
    diff = 0.05 > image > threshold
    extr[diff == 0] = 0
    return np.nonzero(extr)


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
    plt.plot(coord[1],coord[0],'*',color='r')


def pyramid(image, blur_nbr, k, sigma):
    res_shape=(blur_nbr, image.shape[0], image.shape[1])
    res_img = np.zeros(res_shape)
    fimage = np.float64(image)
    prev_img = cv2.GaussianBlur(fimage,(0,0),sigmaX=sigma, sigmaY=sigma)

    for i in range(0, blur_nbr):
        blurred_img = cv2.GaussianBlur(prev_img,(0,0),sigmaX=k*sigma, sigmaY=k*sigma)
        res_img[i] = prev_img - blurred_img
        prev_img = blurred_img
    return res_img

# img2 = cv2.imread('fontanna2.jpg')
# img1 = cv2.imread('fontanna1.jpg')
img1 = cv2.imread('budynek1.jpg')
img2 = cv2.imread('budynek2.jpg')

img1G = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2G = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ksize = 7
threshold = 0.1
sigma = 1.6
k = 1.26
# img1_H = calcH(img1, ksize)
# img2_H = calcH(img2, ksize)

img1_p = pyramid(img1, 5, k, sigma)
img2_p = pyramid(img2, 5, k, sigma)

max_img1 = find_extr(img1_p, ksize, threshold)
max_img2 = find_extr(img2_p, ksize, threshold)

draw_max(img1, max_img1)
draw_max(img2, max_img2)
x = 10
plt.show()











