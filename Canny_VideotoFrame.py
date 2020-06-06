from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pylab
import imageio
import cv2  

videos_path = 'D:/Code/Python-DeepLearning/Canny/Video2.mp4'
frames_save_path = 'D:/Code/Python-DeepLearning/Canny/Frame'


cap = cv2.VideoCapture(videos_path)
count = 0
while(1):
    count += 1
    _, frame = cap.read()
    
    img_gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    cv2.imshow('Original',frame)
    edges = cv2.Canny(img_gray,100,200)
    cv2.imshow('Edges',edges)
    cv2.imwrite(frames_save_path + "/frame%d.jpg" % count, edges, [cv2.IMWRITE_JPEG_QUALITY,20])
    img = cv2.cvtColor(edges,cv2.COLOR_GRAY2RGB)
    k = cv2.waitKey(1) & 0xFF
    if k == 24:
        break

cv2.destroyAllWindows()
cap.release()
