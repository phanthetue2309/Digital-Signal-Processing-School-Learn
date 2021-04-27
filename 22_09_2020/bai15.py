import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy 
import cv2

img = mpimg.imread('09.png')
print(img)
imgplot = plt.imshow(img)
lum_img = img[:, :]
plt.imshow(lum_img)

# plt.imshow(lum_img, cmap="gist_rainbow_r")
# plt.show()
# plt.imshow(lum_img, cmap="hot")

# plt.show()

img = cv2.imread('09.png')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)


kernel1 = np.ones((3,3),np.float32)/9
dst1 = cv2.filter2D(img,-1,kernel1)

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(dst),plt.title('B')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(dst1),plt.title('C')
plt.xticks([]), plt.yticks([])

plt.show()