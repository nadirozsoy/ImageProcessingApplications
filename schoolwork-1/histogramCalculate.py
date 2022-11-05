#02185076005
#Nadir Özsoy

from matplotlib import pyplot as plt
import cv2
import numpy as np

#image reading
foto = cv2.imread("planet.jpeg",0)
cv2.imshow("image",foto)

#Histogram calculate
def cal_hist(gray_img):
    hist = np.zeros(shape=(256))
    (h,w) = gray_img.shape
    for i in range(w):
        for j in range(h):
            hist[gray_img[j,i]] += 1
    return hist

plt.plot(cal_hist(foto))
plt.show()