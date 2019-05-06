import numpy as np
import matplotlib.pyplot as plt
import cv2

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
uzupelniony_wzorzecG[:shape_wzor[0], :shape_wzor[1]] = hanning2D(wzorG.shape[0])*wzorG

uzupelniony_wzorzecG_FFT = np.fft.fft2(uzupelniony_wzorzecG)
przeszukiwany_obrazG_FFT = np.fft.fft2(przeszukiwany_obrazG)

# Filtracja górnoprzepustowa
Ampl_uz_wz = highpassFilter(uzupelniony_wzorzecG.shape) * np.abs(uzupelniony_wzorzecG_FFT)
Ampl_prz_obr = highpassFilter(uzupelniony_wzorzecG.shape) * np.abs(przeszukiwany_obrazG_FFT)

# Log-polar
R1 = Ampl_uz_wz.shape[0]//2
R2 = Ampl_prz_obr.shape[0]//2

print(2*R2)
print(np.log(R2))

Log_pol_uz_wz = cv2.logPolar(Ampl_uz_wz, center=(Ampl_uz_wz.shape[0]//2, Ampl_uz_wz.shape[1]//2), M=2*R1/np.log(R1), flags=cv2.INTER_LINEAR + cv2.WARP_FILL_OUTLIERS)
Log_pol_prz_obr = cv2.logPolar(Ampl_prz_obr, center=(Ampl_prz_obr.shape[0]//2, Ampl_prz_obr.shape[1]//2), M=2*R2/np.log(R2), flags=cv2.INTER_LINEAR + cv2.WARP_FILL_OUTLIERS)

Log_pol_uz_wz_FFT = np.fft.fft2(Log_pol_uz_wz)
Log_pol_prz_obr_FFT = np.fft.fft2(Log_pol_prz_obr)

# Korelacja
ccor = Log_pol_prz_obr_FFT * Log_pol_uz_wz_FFT.conj()
R = ccor/np.abs(ccor)
ifft2 = np.fft.ifft2(R)

y,x = np.unravel_index( np.argmax(np.abs(ifft2)), ifft2.shape)


plt.gray()
plt.figure(1)
plt.imshow(wzorG)

plt.figure(2)
plt.imshow(shape_przeszukiwany_obrazG)

plt.figure(3)
plt.imshow(uzupelniony_wzorzecG)

plt.show()
