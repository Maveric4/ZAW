import cv2
import numpy as np
import matplotlib.pyplot as plt

#  kryternia przetwania obliczen (blad+liczba iteracji)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

#przygotowanie punktow 2D w postaci: (0, 0, 0), (1, 0, 0), (2, 0, 0)...., (6, 7, 0)
objp = np.zeros((6 * 7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

# tablice do przechowywania punktow obiektow (3D) i punktow na obrazie (2D)dla wszystkich obrazow
objpointsL = [] # punkty 3d w przestrzeni (rzeczywsite)
objpointsR = [] # punkty 3d w przestrzeni (rzeczywsite)

imgpointsL = [] # punkty 2d w plaszczyznie obrazu.
imgpointsR = [] # punkty 2d w plaszczyznie obrazu.

for i in range(1,13):
    # wczytanie obrazu
    imgL = cv2.imread('images_left/left%02d.jpg' % i)
    imgR = cv2.imread('images_right/right%02d.jpg' % i)
    # konwersja do odcieni szarosci
    grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
    # wyszukiwanie naroznikow na planszy
    retL, cornersL = cv2.findChessboardCorners(grayL, (7, 6), None)
    retR, cornersR = cv2.findChessboardCorners(grayR, (7, 6), None)

    # jesli znaleniono na obrazie punkty
    if retL & retR == True:
        #dolaczenie wspolrzednych 3D
        objpointsL.append(objp)
        # poprawa lokalizacji punktow (podpiskelowo)
        corners2L = cv2.cornerSubPix(grayL, cornersL, (11, 11), (-1, -1), criteria)
        # dolaczenie poprawionych punktow
        imgpointsL.append(corners2L)

        objpointsR.append(objp)
        corners2R = cv2.cornerSubPix(grayR, cornersR, (11, 11), (-1, -1), criteria)
        imgpointsR.append(corners2R)

    # wizualizacja wykrytych naroznikow

    # cv2.drawChessboardCorners(imgL, (7, 6), corners2L, retL)
    # cv2.imshow("CornersL", imgL)
    #
    # cv2.drawChessboardCorners(imgR, (7, 6), corners2R, retR)
    # cv2.imshow("CornersR", imgR)
    # cv2.waitKey(0)

retL, mtxL, distL, rvecsL, tvecsL = cv2.calibrateCamera(objpointsL, imgpointsL,grayL.shape[::-1], None, None)
retR, mtxR, distR, rvecsR, tvecsR = cv2.calibrateCamera(objpointsR, imgpointsR,grayR.shape[::-1], None, None)

# Kalibracja stereo
retval, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, R, T, E, F = cv2.stereoCalibrate(objpointsR,imgpointsL,imgpointsR,mtxL,distL,mtxR,distR,grayL.shape[::-1])

# Rektyfikacja
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, grayR.shape[::-1], R, T)

# Obliczenie wspolczynnikow mapowania dla funkcji repmap
map1_L, map2_L = cv2.initUndistortRectifyMap(cameraMatrix1, distCoeffs1, R1,P1, grayL.shape[::-1], cv2.CV_16SC2)
map1_R, map2_R = cv2.initUndistortRectifyMap(cameraMatrix2, distCoeffs2, R2,P2, grayL.shape[::-1], cv2.CV_16SC2)

dst_L = cv2.remap(imgL, map1_L, map2_L, cv2.INTER_LINEAR)
dst_R = cv2.remap(imgR, map1_R, map2_R, cv2.INTER_LINEAR)

N, XX, YY = dst_L.shape[::-1] # pobranie rozmiarow obrazka (kolorowego)
visRectify = np.zeros((YY,XX*2,N),np.uint8)

# utworzenie nowego obrazka oszerokosci x2
visRectify[:,0:640:,:] = dst_L      # przypisanie obrazka lewego
visRectify[:,640:1280:,:] = dst_R   # przypisanie obrazka prawego#

# Wyrysowanie poziomych linii
for y in range(0,480,10):
    cv2.line(visRectify, (0,y), (1280,y), (255,0,0))

cv2.imshow('visRectify',visRectify)  #wizualizacja
cv2.waitKey(0)
