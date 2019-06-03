#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math # do PI#
import os


kernel_size = 45 # rozmiar rozkladu
mouseX, mouseY = (830,430) # przykladowe wspolrzedne
def track_init(event, x, y, flags, param):
    global mouseX, mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(param, (int(x-kernel_size//2), int(y- kernel_size//2)),(x + kernel_size, y + kernel_size), (0, 255, 0), 2)
        mouseX,mouseY = x,y

# # Wczytanie pierwszego obrazka
I = cv2.imread('track_seq/track00100.png')
# cv2.namedWindow('Tracking')
# cv2.setMouseCallback('Tracking',track_init, param=I)
# # Pobranie klawisza
# while 1:
#     cv2.imshow('Tracking', I)
#     k = cv2.waitKey(20) & 0xFF
#     if k == 27:   # ESC
#         break

#Generowanie Gaussa
# kernel_size = 45                        #rozmiar rozkladu
sigma = kernel_size/6                   # odchylenie std
x = np.arange(0, kernel_size, 1,float)  # wektor poziomy
y = x[:, np.newaxis]                    # wektor pionowy
x0 = y0 = kernel_size // 2              # wsp. srodka
G = 1/(2*math.pi*sigma**2)*np.exp(-0.5*((x-x0)**2 + (y-y0)**2) / sigma**2)

mouseX = 812
mouseY = 406
xS = mouseX-kernel_size//2
yS = mouseY-kernel_size//2
I_HSV = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)

plt.figure(1)
plt.gray()
plt.imshow(I_HSV[:, :, 0])
plt.title('H in HSV')
plt.show()

## Obliczanie histogramu
# I_H = I_HSV[:, :, 0]
# hist_q = np.zeros((256, 1), float)
# for jj in range(0, kernel_size):
#     for ii in range(0, kernel_size):
#         pixel_H = I_H[yS+jj, xS+ii]
#         hist_q[pixel_H] += G[jj, ii]

# Obliczanie histogramu wzorca - Szybciej
I_H = I_HSV[:, :, 0]
hist_q = np.zeros((256, 1), float)
for u in range(256):
    mask = I_H[yS:yS + kernel_size, xS:xS + kernel_size] == u
    hist_q[u] = np.sum(G[mask])

hist_q_norm = hist_q/np.sum(hist_q)

num_imgs = 200
for i in range(101, num_imgs):
    I = cv2.imread('track_seq/track%05d.png' %i)
    I_HSV = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
    I_H = I_HSV[:, :, 0]
    hist_p = np.zeros((256, 1), float)
    for c in range(256):
        mask = I_H[yS:yS + kernel_size, xS:xS + kernel_size] == c
        hist_p[c] = np.sum(G[mask])

    hist_p_norm = hist_p/np.sum(hist_p)
    wsp_Bhattacharyya = np.sqrt(hist_p_norm * hist_q_norm)

    array = np.zeros((kernel_size, kernel_size))
    for jj in range(kernel_size):
        for ii in range(kernel_size):
            array[jj, ii] = wsp_Bhattacharyya[I_H[yS:yS+jj, xS:xS+ii]] * G(jj, ii)

    M = cv2.moments(array)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])

    yS = cy - kernel_size//2
    xS = cx - kernel_size//2


    cv2.rectangle(I, yS, xS)


    cv2.imshow("Video", I)
    cv2.waitKey(1)
















