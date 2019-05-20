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
    sobelx = cv2.Sobel(imgG, cv2.CV_64F, 1, 0, ksize=size)
    sobelxx_bG = sobelx*sobelx
    sobelxx = cv2.GaussianBlur(sobelxx_bG,(size, size), 0)
    sobely = cv2.Sobel(imgG, cv2.CV_64F, 0, 1, ksize=size)
    sobelyy_bG = sobely*sobely
    sobelyy = cv2.GaussianBlur(sobelyy_bG,(size, size), 0)
    sobelxy_bG = sobelx*sobely
    sobelxy = cv2.GaussianBlur(sobelxy_bG,(size, size), 0)

    detM = sobelxx * sobelyy - sobelxy**2
    traceM = sobelxx + sobelyy
    H = detM - k*traceM**2
    return H/H.max()


def draw_max(img, coord, scale):
    x = coord[2]
    y = coord[1]
    # print(coord)
    # print(x)
    # print(y)
    # print(x[coord[0] == scale])
    # print(y[coord[0] == scale])
    plt.imshow(img)
    plt.plot(x[coord[0] == scale], y[coord[0] == scale], '*', color='r')


def pyramid(image, blur_nbr, k, sigma):
    res_shape = (blur_nbr, image.shape[0], image.shape[1])
    res_img = np.zeros(res_shape)
    fimage = np.float64(image)
    prev_img = cv2.GaussianBlur(fimage, (0, 0), sigmaX=sigma, sigmaY=sigma)

    for i in range(0, blur_nbr):
        blurred_img = cv2.GaussianBlur(prev_img, (0, 0), sigmaX=k**i*sigma, sigmaY=k**i*sigma)
        res_img[i] = calcH(blurred_img - prev_img, ksize)
        prev_img = blurred_img
    return res_img


img1 = cv2.imread('fontanna1.jpg')
img2 = cv2.imread('fontanna_pow.jpg')

img1G = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2G = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ksize = 7
threshold = 0.3
sigma = 1.6
k = 1.26
# img1_H = calcH(img1, ksize)
# img2_H = calcH(img2, ksize)

img1_p = pyramid(img1G, 5, k, sigma)
img2_p = pyramid(img2G, 5, k, sigma)
max_img1 = find_max(img1_p, ksize, threshold)
max_img2 = find_max(img2_p, ksize, threshold)

for scale in range(0, 5):
    # Share a X axis with each column of subplots
    # fig = plt.figure(figsize=(18,8))
    plt.figure()
    plt.title("skala " + str(scale))
    # plt.subplot(1, 2, 1)
    draw_max(img1, max_img1, scale)
    # plt.subplot(1, 2, 2)
    plt.figure()
    plt.title("skala " + str(scale))
    draw_max(img2, max_img2, scale)

plt.show()












