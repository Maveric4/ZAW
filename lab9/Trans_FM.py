import cv2
import matplotlib.pyplot as plt
import numpy as np

wzor = cv2.imread("obrazy_Mellin/wzor.pgm")
wzorG = cv2.cvtColor(wzor, cv2.COLOR_BGR2GRAY)
shape_wzor = wzorG.shape
print(shape_wzor)

domek = cv2.imread("obrazy_Mellin/domek_r0.pgm")
domekG = cv2.cvtColor(domek, cv2.COLOR_BGR2GRAY)
shape_domek = domekG.shape



uzupelniony_wzorzec = np.zeros(shape_domek)
uzupelniony_wzorzec[:shape_wzor[0], :shape_wzor[1]] = wzorG



domek_FFT = np.fft.fft2(domekG)
wzor_FFT = np.fft.fft2(uzupelniony_wzorzec)

ccor = domek_FFT * wzor_FFT.conj()
R = ccor/np.abs(ccor)
ifft2 = np.fft.ifft2(R)

y,x = np.unravel_index( np.argmax(np.abs(ifft2)), ifft2.shape)

dx = x
dy = y

macierz_translacji = np.float32([[1,0,dx],[0,1,dy]])  # gdzie dx, dy -wektor przesuniecia
obraz_przesuniety = cv2.warpAffine(uzupelniony_wzorzec, macierz_translacji,(uzupelniony_wzorzec.shape[1], uzupelniony_wzorzec.shape[0]))


plt.gray()
plt.figure(1)
plt.imshow(wzorG)


plt.figure(2)
plt.imshow(domekG)
plt.plot(x, y, '*', color='r')

plt.figure(3)
plt.imshow(uzupelniony_wzorzec)

plt.figure(4)
plt.plot(x, y, '*', color='r')
plt.imshow(obraz_przesuniety)
plt.show()


