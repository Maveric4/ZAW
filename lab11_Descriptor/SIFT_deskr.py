import cv2
import numpy as np
import matplotlib.pyplot as plt

SIFT_obj = cv2.xfeatures2d.SIFT_create()

# img1 = cv2.imread('fontanna1.jpg')
# img2 = cv2.imread('fontanna2.jpg')

img1 = cv2.imread('fontanna1.jpg')
img2 = cv2.imread('fontanna_pow.jpg')

# img1 = cv2.imread('budynek1.jpg')
# img2 = cv2.imread('budynek2.jpg')

img1G = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2G = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

pkt1, descr1 = SIFT_obj.detectAndCompute(img1G, None)
pkt2, descr2 = SIFT_obj.detectAndCompute(img2G, None)

bf = cv2.BFMatcher_create(normType=cv2.NORM_L2)
matches = bf.knnMatch(descr1, descr2, k=2)

best_matches = [[m] for m, n in matches if m.distance < 0.1*n.distance]

img_out = cv2.drawMatchesKnn(img1, pkt1, img2, pkt2, best_matches, None, flags=2)

plt.figure()
plt.imshow(img_out)
plt.show()

