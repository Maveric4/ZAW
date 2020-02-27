#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import convolve1d
import math
from sklearn import svm

def calc_comp_grad(im):
    # Obliczanie gradientow z maska [-1 0 1]
    dx = convolve1d(np.int32(im), np.array([-1, 0, 1]), 1)
    dy = convolve1d(np.int32(im), np.array([-1, 0, 1]), 0)

    grad = np.sqrt(dx**2 + dy**2)
    orient = np.arctan2(dy, dx)
    return grad, orient


im = cv2.imread('pedestrians/pos/per00060.ppm')
# plt.figure()
# plt.title('Person')
# plt.imshow(im)
# plt.show()

def calc_grad(im):
    gradB, orientB = calc_comp_grad(im[:,:,0])
    gradG, orientG = calc_comp_grad(im[:,:,1])
    gradR, orientR = calc_comp_grad(im[:,:,2])

    grad = gradB.copy() # poczatkowo wynikowa macierz to gradient skladowej B
    orient = orientB.copy() # poczatkowo wynikowa macierz to orientacja skladowej B

    m1 = gradB-gradG # m1 - tablica pomocnicza do wyznaczania maksimummiedzy skladowymi B i G
    grad[m1<0] = gradG[m1<0] # w macierzy wynikowej gradienty skladowej B sa podmieniane na wieksze od nich gradienty skladowej G
    orient[m1 < 0] = orientG[m1 < 0]

    m2 = grad - gradR
    grad[m2<0] = gradR[m2<0]
    orient[m2<0] = orientR[m2<0]

    # Zamiana na stopnie
    orient = orient * 180 / np.pi

    # wyzerowac brzegowe piksele
    grad[:, 0] = 0
    grad[:, -1] = 0
    grad[-1, :] = 0
    grad[0, :] = 0

    orient[:, 0] = 0
    orient[:, -1] = 0
    orient[-1, :] = 0
    orient[0, :] = 0

    return grad, orient



cellSize = 8  # rozmiar komorki
YY, XX, z = im.shape
YY_cell = np.int32(YY / cellSize)
XX_cell = np.int32(XX / cellSize)


def calc_block_hist(im, grad, orient, YY_cell, XX_cell):
    # Obliczenia histogramow
    # Kontener na histogramy - zakladamy, ze jest 9 przedzialow
    hist = np.zeros([YY_cell, XX_cell, 9], np.float32)# Iteracja po komorkach na obrazie
    for jj in range(0,YY_cell):
        for ii in range(0,XX_cell): # Wyciecie komorki
            M = grad[jj*cellSize:(jj+1)*cellSize,ii*cellSize:(ii+1)*cellSize]
            T = orient[jj*cellSize:(jj+1)*cellSize,ii*cellSize:(ii+1)*cellSize]
            M = M.flatten()
            T = T.flatten()
            # Obliczenie histogramu
            for k in range(0, cellSize*cellSize):
                m = M[k]
                t = T[k]
                # Usuniecie ujemnych kata (zalozenie katy w stopniach)
                if t < 0:
                    t = t + 180
                # Wyliczenie przezdialu
                t0 = np.floor( (t-10)/20 )*20 +10 # Przedzial ma rozmiar 20,srodek to 20#
                #Przypadek szczegolny tj. t0 ujemny
                if t0 < 0:
                    t0 = 170
                # Wyznaczenie indeksow przedzialu
                i0 =int((t0-10)/20)
                i1 = i0+1
                #Zawijanie
                if i1 == 9:
                    i1=0
                # Obliczenie odleglosci do srodka przedzialu
                d =min(abs(t-t0), 180-abs(t-t0))/20
                # Aktualizacja histogramu
                hist[jj,ii,i0] = hist[jj,ii,i0] + m*(1-d)
                hist[jj,ii,i1] = hist[jj,ii,i1] + m*d

            #Dla przyspieszenia mo ̇zna operacje w p ̨etli k spróbowa ́c zrealizowa ́c macierzowo, wówczasw p ̨etli k pozostanie tylko:diff =abs(T-t0)in range(0,cellSize*cellSize):min(diff[k], 180 - diff[k] )/201[jj,ii,i0[k]] += M[k]*(1-d)1[jj,ii,i1[k]] += M[k]*(d)
    return hist



def calc_feat_vec(hist, YY_cell, XX_cell):
    # Normalizacja w blokach
    e = math.pow(0.00001,2)
    F = []
    for jj in range(0,YY_cell-1):
        for ii in range(0,XX_cell-1):
            H0 = hist[jj,ii,:]
            H1 = hist[jj,ii+1,:]
            H2 = hist[jj+1,ii,:]
            H3 = hist[jj+1,ii+1,:]
            H = np.concatenate((H0, H1, H2, H3))
            n = np.linalg.norm(H)
            Hn = H/np.sqrt(math.pow(n, 2)+e)
            F = np.concatenate((F, Hn))
    return F

#wyswietlanie gradientow obrazu
#defHOGpicture(w, bs): # w - histogramy gradientow obrazu, bs - rozmiarkomorki (u nas 8)bim1 = np.zeros((bs, bs))bim1[np.round(bs//2):np.round(bs//2)+1,:] = 1;bim = np.zeros(bim1.shape+(9,));bim[:,:,0] = bim1;foriin range(0,9):  #2:9,bim[:,:,i] = scipy.misc.imrotate(bim1, -i*20,’nearest’)/255Y,X,Z = w.shapew[w < 0] = 0;im = np.zeros((bs*Y, bs*X));foriin range(Y):iisl = (i)*bsiisu = (i+1)*bsforjin range(X):jjsl = j*bsjjsu=(j+1)*bsforkin range(9):im[iisl:iisu,jjsl:jjsu] += bim[:,:,k]*w[i,j,k];returnim


def calc_HOG(im):
    grad, orient = calc_grad(im)
    hist = calc_block_hist(im, grad, orient, YY_cell, XX_cell)
    return calc_feat_vec(hist, YY_cell, XX_cell)


# feat_vec = calc_HOG(im)
# Klasyfikator SVM
num_imgs = 400
HOG_data = np.zeros([2*num_imgs, 3781], np.float32)
for i in range(0, num_imgs):
    IP = cv2.imread('pedestrians/pos/per%05d.ppm' %(i+1))
    IN = cv2.imread('pedestrians/neg/neg%05d.png' %(i+1))
    F = calc_HOG(IP)
    HOG_data[i, 0] = 1
    HOG_data[i, 1:] = F
    F = calc_HOG(IN)
    HOG_data[i+num_imgs, 0] = 0
    HOG_data[i+num_imgs, 1:] = F

labels = HOG_data[:, 0]
data = HOG_data[:, 1:]

clf = svm.SVC(kernel='linear', C=1.0)
# Przeprowadzamy uczenie:
clf.fit(data, labels)
# Testujemy:
print(data)
lp = clf.predict(data)

TP = [x == 1 for x in lp[:int(np.floor(lp.size/2))]]
FP = [x == 1 for x in lp[int(np.floor(lp.size/2)):]]
TN = [x != 1 for x in lp[int(np.floor(lp.size/2)):]]
FN = [x != 1 for x in lp[:int(np.floor(lp.size/2))]]
print(TP)
print(TN)
print("Accuracy: ", (np.sum(TP) + np.sum(TN))/lp.size*100, "%")

# Detekcja na obrazie rzeczywistym
#
import cv2
test = cv2.imread('pedestrians/pos/per00060.ppm')
# print(test.shape)
for i in range(1, 5):
    im = cv2.imread('testImages/testImage%d.png' %i)
    # print(im.shape[0])
    im_show = im.copy()

    # print(test.shape)
    # print(IP.shape)
    # IP[:test.shape[0], :test.shape[1], :] = test
    step = 16
    print(im.shape)
    for ii in range(0, im.shape[0]-test.shape[0], step):
        for jj in range(0, im.shape[1]-test.shape[1], step):
            frag = im[ii:ii+test.shape[0], jj:jj+test.shape[1], :]
            # print("frag", frag)
            feat_vec = calc_HOG(frag)
            # print(feat_vec.reshape(1, -1))
            isHuman = clf.predict(feat_vec.reshape(1, -1))
            # print("predicted is Human: ", isHuman)
            if isHuman:
                cv2.rectangle(im_show, (jj, ii), (jj + test.shape[1], ii + test.shape[0]), color=(0, 0, 255), thickness=1)
                plt.figure()
                plt.imshow(frag)
                print("found")

        print(ii, " / ", im.shape[0] - test.shape[0])
    plt.figure()
    plt.imshow(im_show)
    # cv2.imshow("Real Image", im_show)
    # cv2.waitKey(0)

plt.show()


