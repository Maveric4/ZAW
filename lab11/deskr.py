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

def find_descr(img, pts, size):
    X, Y = img.shape[0], img.shape[1]
    pts = list(filter(lambda pt: Y - size > pt[0] >= size and X - size > pt[1] >= size, zip(pts[0],pts[1])))
    descr = []
    for pt in pts:
        frag = img[(pt[0]-size//2):(pt[0]+size//2), (pt[1]-size//2):(pt[1]+size//2)]
        descr.append(frag.flatten())

    return list(zip(descr, pts))


def find_simil(descr1, descr2, nbr_sim_el):
    lst = []
    for obj1 in descr1:
        for obj2 in descr2:
            dist = np.linalg.norm(obj1[0] - obj2[0])
            lst.append(list((obj1[1], dist)))
            # print(dist)
            # print(obj1)
            # print(obj2)


    lst.sort(key=lambda x: x[1])
    return lst[:nbr_sim_el]


def draw_max(img, coord):
    plt.figure()
    plt.imshow(img)
    plt.plot(coord[1], coord[0], '*', color='r')


img1 = cv2.imread('fontanna1.jpg')
img2 = cv2.imread('fontanna2.jpg')

img1G = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2G = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ksize = 5
threshold = 0.3
descr_size = 4
nbr_sim_el = 15

img1_H = calcH(img1G, ksize)
img2_H = calcH(img2G, ksize)

max_img1 = find_max(img1_H, ksize, threshold)
max_img2 = find_max(img2_H, ksize, threshold)

pts_descr1 = find_descr(img1G, max_img1, descr_size)
pts_descr2 = find_descr(img2G, max_img2, descr_size)
# print(pts_descr1)

found_pts = find_simil(pts_descr1, pts_descr2, nbr_sim_el)
# print(found_pts)
lst_x = [x[0][0] for x in found_pts]
lst_y = [x[0][1] for x in found_pts]
print(lst_x)
lst = np.c_[lst_x,lst_y]
print(lst)
draw_max(img1, lst)
plt.show()


x = 10













