#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage.filters as filters
import pm


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
    pts = list(filter(lambda pt: Y - size > pt[0] >= size and X - size > pt[1] >= size, zip(pts[0], pts[1])))
    descr = []
    for pt in pts:
        frag = img[(pt[0]-size//2):(pt[0]+size//2), (pt[1]-size//2):(pt[1]+size//2)]
        frag_mean = np.mean(frag)
        den = np.std(frag - frag_mean)
        frag_af = (frag - frag_mean)/den
        descr.append(frag_af.flatten())
        # print(frag_af.flatten())
    return list(zip(descr, pts))


def find_simil(descr1, descr2, nbr_sim_el):
    lst = []
    for obj1 in descr1:
        for obj2 in descr2:
            dist = np.linalg.norm(obj1[0] - obj2[0])
            lst.append(list(((obj1[1], obj2[1]), dist, obj1[0], obj2[0])))

    lst.sort(key=lambda x: x[1])
    # print(lst[:nbr_sim_el])
    # for x in lst[:nbr_sim_el]:
    #     print(x)
    return [x[0] for x in lst[:nbr_sim_el]]
    # return = [x[0] for x in list(filter(lambda x: x[1] < 0.5, lst))]


def draw_found_matches(img1, img2, coord):
    plt.figure(figsize=(10, 10))
    plt.imshow(img1)
    plt.plot([x[0][1] for x in coord], [x[0][0] for x in coord], '*', color='r')
    plt.figure(figsize=(10, 10))
    plt.imshow(img2)
    plt.plot([x[1][1] for x in coord], [x[1][0] for x in coord], '*', color='r')


def show_same_matches(img1, img2, coord):
    import random
    # colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.imshow(img1)
    ax2.imshow(img2)
    for i, pts in enumerate(coord):
        r = lambda: random.randint(0, 255)
        color = '#%02X%02X%02X' % (r(), r(), r())
        ax1.plot(pts[0][1], pts[0][0], '*', color=color) #colors[i%8])
        ax2.plot(pts[1][1], pts[1][0], '*', color=color) #colors[i%8])


def draw_max(img, coord):
    plt.figure()
    plt.imshow(img)
    plt.plot(coord[1], coord[0], '*', color='r')


# img1 = cv2.imread('budynek1.jpg')
# img2 = cv2.imread('budynek2.jpg')
img1 = cv2.imread('fontanna1.jpg')
img2 = cv2.imread('fontanna2.jpg')
# img1 = cv2.imread('eiffel1.jpg') #different sizes
# img2 = cv2.imread('eiffel2.jpg') #different sizes


img1G = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2G = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ksize = 7
threshold = 0.1
descr_size = 4
nbr_sim_el = 20

img1_H = calcH(img1G, ksize)
img2_H = calcH(img2G, ksize)

max_img1 = find_max(img1_H, ksize, threshold)
# draw_max(img1, max_img1)
max_img2 = find_max(img2_H, ksize, threshold)
# draw_max(img2, max_img2)

pts_descr1 = find_descr(img1G, max_img1, descr_size)
pts_descr2 = find_descr(img2G, max_img2, descr_size)
#print(pts_descr1)

found_pts = find_simil(pts_descr1, pts_descr2, nbr_sim_el)
# # print(found_pts)

show_same_matches(img1, img2, found_pts)


draw_found_matches(img1, img2, found_pts)
pm.plot_matches(img1, img2, found_pts)
plt.show()















