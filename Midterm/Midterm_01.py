# -*- coding: utf-8 -*-
from PIL import Image
from pylab import *

im = array(Image.open('../data/empire.jpg'))

imshow(im)

x = [100, 400, 100, 400]    #x座標的點
y = [200, 500, 200, 500]    #y座標的點

#axis('off')

#原圖
pil_im = Image.open('../data/empire.jpg')
subplot(121)
imshow(pil_im)

#旋轉後的圖
pil_im = Image.open('../data/empire.jpg')
pil_im = pil_im.rotate(45)
subplot(122)
imshow(pil_im)

show()