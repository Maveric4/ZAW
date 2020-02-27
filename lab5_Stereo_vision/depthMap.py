from __future__ import print_function
import sys
import numpy as np
import cv2

imgL = cv2.pyrDown(cv2.imread('aloes/aloeL.jpg') )
imgR = cv2.pyrDown(cv2.imread('aloes/aloeR.jpg') )

min_disp = 16
num_disp = 128 - min_disp
window_size = 11
stereoBM = cv2.StereoBM_create(numDisparities=num_disp, blockSize=window_size)
stereoBM.setMinDisparity(min_disp)
stereoBM.setNumDisparities(num_disp)
stereoBM.setBlockSize(window_size)
stereoBM.setUniquenessRatio(1)
stereoBM.setSpeckleRange(32)
stereoBM.setSpeckleWindowSize(100)

stereoSGBM = cv2.StereoSGBM_create(numDisparities=num_disp, blockSize=window_size)
stereoSGBM.setMinDisparity(min_disp)
stereoSGBM.setNumDisparities(num_disp)
stereoSGBM.setBlockSize(window_size)
#stereoSGBM.setDisp12MaxDiff(0)
#stereoSGBM.setUniquenessRatio(1)
stereoSGBM.setSpeckleRange(32)
stereoSGBM.setSpeckleWindowSize(100)

grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
dispBM = stereoBM.compute(grayL, grayR).astype(np.float32) / 16.0
disp_mapBM = (dispBM - min_disp)/num_disp

dispSGBM = stereoSGBM.compute(grayL, grayR).astype(np.float32) / 16.0
disp_mapSGBM = (dispSGBM - min_disp)/num_disp


cv2.imshow('Disparity BM', disp_mapBM)
cv2.imshow('Disparity SGBM', disp_mapSGBM)

cv2.waitKey()
cv2.destroyAllWindows()