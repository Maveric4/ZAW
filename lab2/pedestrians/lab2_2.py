import cv2
import numpy as np

f =open('temporalROI.txt','r')       # otwarcie pliku
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
FP = 0;
# TN = 0


I = cv2.imread('input/in%06d.jpg' %300)
IG_t = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
for i in range(roi_start, roi_end):
    I = cv2.imread('input/in%06d.jpg' % i)
    IG_t2 = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    B = cv2.threshold(cv2.absdiff(IG_t,IG_t2), 12, 255, cv2.THRESH_BINARY)
    B = B[1]
    kernel = np.ones((3, 3), np.uint8)
    erosion = cv2.erode(B, kernel, iterations=1)
    dilation = cv2.dilate(erosion, kernel, iterations=1)
    cv2.imshow("I1", dilation)
    medianBlur_img = cv2.medianBlur(dilation,5)
    cv2.imshow("I2", medianBlur_img)
    cv2.waitKey(1)
    retval, labels, stats, centroids = cv2.connectedComponentsWithStats(medianBlur_img)
    cv2.imshow("Labels", np.uint8(labels / stats.shape[0] * 255))
    if (stats.shape[0] > 1):  # czy sa jakies obiekty
        tab = stats[1:,4] # wyciecie 4 kolumny bez pierwszego elementu
        pi = np.argmax( tab )# znalezienie indeksu najwiekszego elementu
        pi = pi + 1 # inkrementacja bo chcemy indeks w stats, a nie w tab
        # wyrysownie bbox
        cv2.rectangle(I,(stats[pi,0],stats[pi,1]),(stats[pi,0]+stats[pi,2],stats[pi,1]+stats[pi,3]),(255,0,0),2)
        # wypisanie informacji o polu i numerze najwiekszego elementu
        cv2.putText(I,"%f" % stats[pi,4],(stats[pi,0],stats[pi,1]),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0))
        cv2.putText(I,"%d" %pi,(np.int(centroids[pi,0]),np.int(centroids[pi,1])),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    cv2.imshow("I color", I)
    cv2.imshow("bin", B)
    IG_t = IG_t2

    GTB = I = cv2.imread('groundtruth/gt%06d.png' %i)
    GTB_G = cv2.cvtColor(GTB, cv2.COLOR_BGR2GRAY)
    #iloczyn logiczny odpowiednich elementow macierzy

    TP_M = np.logical_and(( medianBlur_img == 255), (GTB_G == 255))
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

print(R)
print(P)
print(F1)

