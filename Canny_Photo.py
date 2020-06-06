import cv2
import matplotlib.pyplot as plt
from skimage import feature
import numpy as np
import scipy.misc

 
im = cv2.imread('Photo.jpg')
img_gray = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
edges = feature.canny(img_gray)
# scipy.misc.toimage(edges).save('edge.jpg')


plt.imshow(edges)
plt.show()

