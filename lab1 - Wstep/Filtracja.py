import cv2

I = cv2.imread('lena.png')
# I = cv2.imread('mandril.jpg')
IG = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# #Filtracja Gaussa
# I_Gauss = cv2.GaussianBlur(IG, ksize=(15, 15), sigmaX=4)
#
# cv2.imshow("IMG", IG)
# cv2.waitKey(0)
# cv2.imshow("Gauss", I_Gauss)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #Filtracja Sobela
# I_Sobel1 = cv2.Sobel(IG, dx=1, dy=1, ddepth=-1)
# I_Sobel2 = cv2.Sobel(IG, dx=2, dy=2, ddepth=-1)
# # I_Sobel3 = cv2.Sobel(IG, dx=3, dy=3, ddepth=-1)
#
# cv2.imshow("IMG", IG)
# cv2.waitKey(0)
# cv2.imshow("Sobel - order 1", I_Sobel1)
# cv2.waitKey(0)
# cv2.imshow("Sobel - order 2", I_Sobel2)
# cv2.waitKey(0)
# # cv2.imshow("Sobel - order 3", I_Sobel3)
# # cv2.waitKey(0)
# cv2.destroyAllWindows()

# #Laplasjan
# I_Laplace = cv2.Laplacian(IG,ddepth=-1)
#
# cv2.imshow("IMG", IG)
# cv2.waitKey(0)
# cv2.imshow("Laplacian", I_Laplace)
# cv2.waitKey(0)

#mediana
I_median1 = cv2.medianBlur(IG, ksize=1)
I_median3 = cv2.medianBlur(IG, ksize=3)
I_median5 = cv2.medianBlur(IG, ksize=5)
I_median7 = cv2.medianBlur(IG, ksize=7)

cv2.imshow("IMG", IG)
cv2.waitKey(0)
cv2.imshow("Median1", I_median1)
cv2.waitKey(0)
cv2.imshow("Median3", I_median3)
cv2.waitKey(0)
cv2.imshow("Median5", I_median5)
cv2.waitKey(0)
cv2.imshow("Median7", I_median7)
cv2.waitKey(0)
