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
TP_mean = 0
FN_mean = 0
FP_mean = 0

TP_median = 0
FN_median  = 0
FP_median  = 0
# TN = 0

alpha = 0.01
I = cv2.imread('pedestrians/input/in%06d.jpg' %roi_start)
BG_mean = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
BG_median = BG_mean
for i in range(roi_start, roi_end):
    I = cv2.imread('pedestrians/input/in%06d.jpg' % i)
    IG = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)*1.0

    BG__mean_prev = BG_mean
    BG_mean = alpha*IG + (1.0-alpha)*BG__mean_prev

    I_mean_diff = cv2.absdiff(BG_mean, IG)
    B_mean = cv2.threshold(I_mean_diff, 30, 255, cv2.THRESH_BINARY)
    B_mean = B_mean[1]
    kernel_mean = np.ones((3, 3), np.uint8)
    erosion_mean = cv2.erode(B_mean, kernel_mean , iterations=1)
    dilation_mean = np.uint8(cv2.dilate(erosion_mean , kernel_mean , iterations=1))

    medianBlur_img_mean = cv2.medianBlur(dilation_mean ,5)
    cv2.imshow("I1_mean", medianBlur_img_mean)

    cv2.waitKey(1)

    retval_mean, labels_mean, stats_mean, centroids_mean = cv2.connectedComponentsWithStats(medianBlur_img_mean)
    cv2.imshow("Labels_mean", np.uint8(labels_mean / stats_mean.shape[0] * 255))
    if (stats_mean.shape[0] > 1):  # czy sa jakies obiekty
        tab_mean = stats_mean[1:,4] # wyciecie 4 kolumny bez pierwszego elementu
        pi_mean = np.argmax( tab_mean )# znalezienie indeksu najwiekszego elementu
        pi_mean = pi_mean + 1 # inkrementacja bo chcemy indeks w stats, a nie w tab
        # wyrysownie bbox
        cv2.rectangle(I,(stats_mean[pi_mean,0],stats_mean[pi_mean,1]),(stats_mean[pi_mean,0]+stats_mean[pi_mean,2],stats_mean[pi_mean,1]+stats_mean[pi_mean,3]),(255,0,0),2)
        # wypisanie informacji o polu i numerze najwiekszego elementu
        cv2.putText(I,"%f" % stats_mean[pi_mean,4],(stats_mean[pi_mean,0],stats_mean[pi_mean,1]),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0))
        cv2.putText(I,"%d" %pi_mean,(np.int(centroids_mean[pi_mean,0]),np.int(centroids_mean[pi_mean,1])),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
    cv2.imshow("I color_mean", I)

    BG__median_prev = BG_median
    # #Iteration over all image
    # for k in range(BG_median.shape[0]):
    #     for l in range(BG_median.shape[1]):
    #         if BG__median_prev[k,l] < IG[k,l]:
    #             BG_median[k,l] = BG__median_prev[k,l] + 1.0
    #         elif BG__median_prev[k,l] > IG[k,l]:
    #             BG_median[k,l] = BG__median_prev[k,l] - 1.0
    #         else:
    #             BG_median[k,l] = BG__median_prev[k,l]*1.0

    less = BG_median < IG
    more = BG_median > IG

    #podejscie liberalne
    BG_median -= more
    BG_median += less

    # #podejscie konserwatywne
    # if i != roi_start:
    #     BG_median -= more * np.uint8(B_median)
    #     BG_median += less * np.uint8(B_median)

    I_median_diff = cv2.absdiff(BG_median*1.0, IG)
    B_median = cv2.threshold(I_median_diff, 12, 255, cv2.THRESH_BINARY)
    B_median = B_median[1]
    kernel_median = np.ones((3, 3), np.uint8)
    erosion_median = cv2.erode(B_median, kernel_median, iterations=1)
    dilation_median = np.uint8(cv2.dilate(erosion_median, kernel_median, iterations=1))

    medianBlur_img_median = cv2.medianBlur(dilation_median, 5)
    cv2.imshow("I1_median", medianBlur_img_median)

    retval_median, labels_median, stats_median, centroids_median = cv2.connectedComponentsWithStats(medianBlur_img_median)
    cv2.imshow("Labels_median", np.uint8(labels_median / stats_median.shape[0] * 255))
    if (stats_median.shape[0] > 1):  # czy sa jakies obiekty
        tab_median = stats_median[1:,4] # wyciecie 4 kolumny bez pierwszego elementu
        pi_median = np.argmax( tab_median )# znalezienie indeksu najwiekszego elementu
        pi_median = pi_median + 1 # inkrementacja bo chcemy indeks w stats, a nie w tab
        # wyrysownie bbox
        cv2.rectangle(I,(stats_median[pi_median,0],stats_median[pi_median,1]),(stats_median[pi_median,0]+stats_median[pi_median,2],stats_median[pi_median,1]+stats_median[pi_median,3]),(255,0,0),2)
        # wypisanie informacji o polu i numerze najwiekszego elementu
        cv2.putText(I,"%f" % stats_median[pi_median,4],(stats_median[pi_median,0],stats_median[pi_median,1]),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0))
        cv2.putText(I,"%d" %pi_median,(np.int(centroids_median[pi_median,0]),np.int(centroids_median[pi_median,1])),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))

    cv2.imshow("I color_median", I)


    GTB = I = cv2.imread('pedestrians/groundtruth/gt%06d.png' %i)
    GTB_G = cv2.cvtColor(GTB, cv2.COLOR_BGR2GRAY)
    #iloczyn logiczny odpowiednich elementow macierzy

    TP_M_mean = np.logical_and(( medianBlur_img_mean == 255), (GTB_G == 255))
    FN_M_mean = np.logical_and((medianBlur_img_mean == 0), (GTB_G == 255))
    FP_M_mean = np.logical_and((medianBlur_img_mean == 255), (GTB_G != 255))

    TP_S_mean = np.sum(TP_M_mean)
    FN_S_mean = np.sum(FN_M_mean)
    FP_S_mean = np.sum(FP_M_mean)
    # suma elementow w macierzy
    TP_mean = TP_mean + TP_S_mean
    FN_mean = FN_mean + FN_S_mean
    FP_mean = FP_mean + FP_S_mean

    TP_M_median = np.logical_and(( medianBlur_img_median == 255), (GTB_G == 255))
    FN_M_median = np.logical_and((medianBlur_img_median == 0), (GTB_G == 255))
    FP_M_median = np.logical_and((medianBlur_img_median == 255), (GTB_G != 255))

    TP_S_median = np.sum(TP_M_median)
    FN_S_median = np.sum(FN_M_median)
    FP_S_median = np.sum(FP_M_median)
    # suma elementow w macierzy
    TP_median = TP_median + TP_S_median
    FN_median = FN_median + FN_S_median
    FP_median = FP_median + FP_S_median



#Obliczone wskazniki
R_mean = TP_mean/(TP_mean + FN_mean)
P_mean = TP_mean/(TP_mean + FP_mean)
F1_mean = 2*P_mean*R_mean/(P_mean + R_mean)

R_median = TP_median/(TP_median + FN_median)
P_median = TP_median/(TP_median + FP_median)
F1_median = 2*P_median*R_median/(P_median + R_median)

print("R mean")
print(R_mean)
print("P mean")
print(P_mean)
print("F1 mean")
print(F1_mean)
print()
print("R median")
print(R_median)
print("P median")
print(P_median)
print("F1 median")
print(F1_median)