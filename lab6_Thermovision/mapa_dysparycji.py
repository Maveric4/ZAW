import  cv2
import numpy as np
import matplotlib.pyplot as plt


def rms(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


left_img = cv2.imread('aloes/aloeL.png')
right_img = cv2.imread('aloes/aloeR.png')
groundtruth = cv2.imread('aloes/')

# First attempt
stereo_bm = cv2.StereoBM_create(16, 7)
dispmap_bm = stereo_bm.compute(cv2.cvtColor(left_img, cv2.COLOR_BGR2GRAY), cv2.cvtColor(right_img, cv2.COLOR_BGR2GRAY))

stereo_sgbm = cv2.StereoSGBM_create(0, 16)
dispmap_sgbm = stereo_sgbm.compute(left_img, right_img)


plt.figure(figsize=(12,10))
plt.subplot(221)
plt.title('left')
plt.imshow(left_img[:,:,[2,1,0]])
plt.subplot(222)
plt.title('right')
plt.imshow(right_img[:,:,[2,1,0]])
plt.subplot(223)
plt.title('BM')
plt.imshow(dispmap_bm, cmap='gray')
plt.subplot(224)
plt.title('SGBM')
plt.imshow(dispmap_sgbm, cmap='gray')
plt.show()


# # Second attempt
# stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
# # stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET, ndisparities=16, SADWindowSize=15)
# disparity = stereo.compute(left_img, right_img)
# plt.imshow(disparity, 'gray')
# plt.show()

print(cv2.__version__)
print(rms())
