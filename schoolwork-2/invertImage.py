#02185076005
#Nadir Özsoy

#Invert Image

import cv2
import numpy as np

#image reading
image = cv2.imread("car.jpeg",0)
cv2.imshow("original",image)

#manuel invert
[h,w] = image.shape
new_image = np.zeros([h,w], dtype=np.uint8)
for i in range(h):
    for j in range(w):
        new_image[i,j] = 255 - image[i,j]
print(image[0,0])
cv2.imshow("Manuel_inverted",new_image)


#invert image reverse
inverted = np.invert(image)
cv2.imshow("inverted",inverted)
negimage = 255 - image
cv2.waitKey()