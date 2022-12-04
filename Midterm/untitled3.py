import cv2
import matplotlib.pyplot as plt

originalImage = cv2.imread('../data/lena.jpg')
img = cv2.imread('../data/lena.jpg',0) #直接读为灰度图像
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
images = [originalImage,thresh1]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.xticks([]),plt.yticks([])
plt.show()
