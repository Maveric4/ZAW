import cv2
import numpy as np

f =open('pedestrians/temporalROI.txt','r')       # otwarcie pliku
line = f.readline()
# odczyt lini
roi_start, roi_end = line.split()
# rozbicie lini na poszczegolneframgenty tesktu
roi_start =int(roi_start)
# konwersja na int
roi_end =int(roi_end)

#Liczniki
TP = 0
FN = 0
FP = 0

backgroundSubtractor = cv2.createBackgroundSubtractorMOG2(history=110, varThreshold=24, detectShadows=False)

for i in range(roi_start, roi_end):
    I_frame = cv2.imread('pedestrians/input/in%06d.jpg' % i)
    IG = cv2.cvtColor(I_frame, cv2.COLOR_BGR2GRAY)
    BG = backgroundSubtractor.apply(image=IG, learningRate=-1)

    kernel = np.ones((3, 3), np.uint8)
    erosion = cv2.erode(BG, kernel, iterations=1)
    dilation = np.uint8(cv2.dilate(erosion, kernel, iterations=1))
    medianBlur_img = cv2.medianBlur(dilation, 5)
    cv2.imshow("IG", IG)
    cv2.imshow("MOG BG", BG)
    cv2.imshow("MOG medianBlur", medianBlur_img)

    GTB = cv2.imread('pedestrians/groundtruth/gt%06d.png' %i)
    GTB_G = cv2.cvtColor(GTB, cv2.COLOR_BGR2GRAY)
    cv2.waitKey(1)

    #iloczyn logiczny odpowiednich elementow macierzy
    TP_M = np.logical_and((medianBlur_img == 255), (GTB_G == 255))
    FN_M = np.logical_and((medianBlur_img == 0), (GTB_G == 255))
    FP_M = np.logical_and((medianBlur_img == 255), (GTB_G != 255))

    TP_S = np.sum(TP_M)
    FN_S = np.sum(FN_M)
    FP_S = np.sum(FP_M)

    # suma elementow w macierzy
    TP = TP + TP_S
    FN = FN + FN_S
    FP = FP + FP_S

#Obliczone wskazniki
R = TP/(TP + FN)
P = TP/(TP + FP)
F1 = 2*P*R/(P + R)

print("R")
print(R)
print("P")
print(P)
print("F1")
print(F1)
