import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
import copy

def hanning2D(n):
    h = np.hanning(n)
    return np.sqrt(np.outer(h,h))

def highpassFilter(size):
    rows = np.cos(np.pi*np.matrix([-0.5 + x/(size[0]-1) for x in range(size[0])]))
    cols = np.cos(np.pi*np.matrix([-0.5 + x/(size[1]-1) for x in range(size[1])]))
    X = np.outer(rows,cols)
    return(1.0 - X)*(2.0 - X)



wzor = cv2.imread("obrazy_Mellin/domek_r0_64.pgm")
wzorG = cv2.cvtColor(wzor, cv2.COLOR_BGR2GRAY)
shape_wzor = wzorG.shape
print(shape_wzor)

przeszukiwany_obraz = cv2.imread("obrazy_Mellin/domek_r30.pgm")
przeszukiwany_obrazG = cv2.cvtColor(przeszukiwany_obraz, cv2.COLOR_BGR2GRAY)
shape_przeszukiwany_obrazG = przeszukiwany_obrazG.shape

uzupelniony_wzorzecG = np.zeros(shape_przeszukiwany_obrazG)
uzupelniony_wzorzecG_copy = copy.deepcopy(uzupelniony_wzorzecG)
uzupelniony_wzorzecG_copy[:shape_wzor[0], :shape_wzor[1]] = wzorG
uzupelniony_wzorzecG[:shape_wzor[0], :shape_wzor[1]] = hanning2D(wzorG.shape[0])*wzorG

uzupelniony_wzorzecG_FFT = np.fft.fft2(uzupelniony_wzorzecG)
przeszukiwany_obrazG_FFT = np.fft.fft2(przeszukiwany_obrazG)

# fftshift()
uzupelniony_wzorzecG_FFT = np.fft.fftshift(uzupelniony_wzorzecG_FFT)
przeszukiwany_obrazG_FFT = np.fft.fftshift(przeszukiwany_obrazG_FFT)

# Filtracja górnoprzepustowa
Ampl_uz_wz = highpassFilter(uzupelniony_wzorzecG.shape) * np.abs(uzupelniony_wzorzecG_FFT)
Ampl_prz_obr = highpassFilter(uzupelniony_wzorzecG.shape) * np.abs(przeszukiwany_obrazG_FFT)

# Log-polar
R1 = Ampl_uz_wz.shape[0]//2
print("R1",R1)
R2 = Ampl_prz_obr.shape[0]//2

M = 2*R1/np.log(R1)
Log_pol_uz_wz = cv2.logPolar(Ampl_uz_wz, center=(Ampl_uz_wz.shape[0]//2, Ampl_uz_wz.shape[1]//2), M=M, flags=cv2.INTER_LINEAR + cv2.WARP_FILL_OUTLIERS)
Log_pol_prz_obr = cv2.logPolar(Ampl_prz_obr, center=(Ampl_prz_obr.shape[0]//2, Ampl_prz_obr.shape[1]//2), M=2*R2/np.log(R2), flags=cv2.INTER_LINEAR + cv2.WARP_FILL_OUTLIERS)

# 2D FFT
Log_pol_uz_wz_FFT = np.fft.fft2(Log_pol_uz_wz)
Log_pol_prz_obr_FFT = np.fft.fft2(Log_pol_prz_obr)

# fftshift()
Log_pol_uz_wz_FFT = np.fft.fftshift(Log_pol_uz_wz_FFT)
Log_pol_prz_obr_FFT = np.fft.fftshift(Log_pol_prz_obr_FFT)

# Korelacja
ccor = Log_pol_prz_obr_FFT * Log_pol_uz_wz_FFT.conj()
R = ccor/np.abs(ccor)
ifft2 = np.fft.ifft2(R)

wsp_kata, wsp_logr = np.unravel_index(np.argmax(np.abs(ifft2)), ifft2.shape)
print(wsp_kata, wsp_logr)
print(ifft2.shape)
# Skalowanie i stopnie
rozmiar_wsp_logr = ifft2.shape[0]

if wsp_logr > rozmiar_wsp_logr//2:
    wykl = rozmiar_wsp_logr - wsp_logr
else:
    wykl = - wsp_logr

rozmiar_wsp_kata = ifft2.shape[0]
A = (wsp_kata * 360.0) / rozmiar_wsp_kata
# Katy sa dwa, gdyz ze wzgledu na symetrie modułu widma czestotliwosciowego wykrywane
# s a obroty tylko do 180 stopni. Dlatego w nastepnym kroku trzeba sprawdzic oba katy i
# wybrac ten, który daje lepsza korelacje
kat1 = - A
kat2 = 180 - A


R1 = ifft2.shape[0]//2
print("R1", R1)
M = 2*R1/np.log(R1)
print(wykl)

skala = np.exp(wykl/M)
print(kat1, skala)

srodekTrans = [math.floor((uzupelniony_wzorzecG_copy.shape[0] + 1) / 2), math.floor((uzupelniony_wzorzecG_copy.shape[1] + 1) / 2)]
print(srodekTrans)
macierz_translacji = cv2.getRotationMatrix2D((srodekTrans[0], srodekTrans[1]), kat1, skala)
print(macierz_translacji)
obraz_trans = cv2.warpAffine(uzupelniony_wzorzecG_copy, macierz_translacji, (uzupelniony_wzorzecG_copy.shape[1], uzupelniony_wzorzecG_copy.shape[0]))

# 2D FFT
obraz_trans_FFT = np.fft.fft2(obraz_trans)

# fftshift()
obraz_trans_FFT = np.fft.fftshift(obraz_trans_FFT)

# Korelacja
ccor = obraz_trans_FFT.conj() * przeszukiwany_obrazG_FFT
R = ccor/np.abs(ccor)
ifft2 = np.fft.ifft2(R)

y, x = np.unravel_index( np.argmax(np.abs(ifft2)), ifft2.shape)

dx = x
dy = y
print(x, y)
macierz_translacji = np.float32([[1,0,dx],[0,1,dy]])  # gdzie dx, dy -wektor przesuniecia
obraz_przesuniety = cv2.warpAffine(obraz_trans, macierz_translacji, (obraz_trans.shape[1], obraz_trans.shape[0]))


plt.gray()
plt.figure(1)
plt.imshow(wzorG)

plt.figure(2)
plt.imshow(przeszukiwany_obrazG)

plt.figure(3)
plt.imshow(uzupelniony_wzorzecG)

plt.figure(4)
plt.plot(x, y, '*', color='r')
plt.imshow(obraz_przesuniety)

plt.show()
