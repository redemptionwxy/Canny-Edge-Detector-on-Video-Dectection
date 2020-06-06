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


    # width = img.shape[1]
    # height = img.shape[0]
    # for y in range (width):
    #   for x in range (height):
    #     if (img[x,y][0]==0 and img[x,y][1]==0 and img[x,y][2]==0):
    #       img[x,y]=(43,32,42)

    # final = cv2.add(img,frame)
    # cv2.imshow('Final',final)
    # cv2.imwrite(frames_save_path + "/frame%d.png" % count, final,[cv2.IMWRITE_PNG_COMPRESSION,5])

    k = cv2.waitKey(1) & 0xFF
    if k == 24:
        break

cv2.destroyAllWindows()
cap.release()
# # from skimage import io
# # from skimage import feature

# def videotoframe():
# # def videotoframe(videos_path,frames_save_path,time_interval):
#   cap = cv2.VideoCapture(0)  
#   # count = 0
#   while (1):
#     _, frame = cap.read()
#     # count += 1
#     # if count % time_interval == 0:
#       # hsv = cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
#     img_gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
#       # img_gray = cv2.imread(frame,0)
#     cv2.imshow('Original',frame)
#     edges = cv2.Canny(img_gray,40,240)
#       # height, weight = img_gray.shape
#     cv2.imshow('Edges',edges)
#       # plt.axis('off')
#       # fig = plt.gcf()
#       # fig.set_size_inches(height/300,weight/300)
#       # plt.gca().xaxis.set_major_locator(plt.NullLocator())
#       # plt.gca().yaxis.set_major_locator(plt.NullLocator())
#       # plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
#       # plt.margins(0,0)
#       # plt.imshow(edges,cmap='gray')
#       # plt.savefig(frames_save_path + "/frame%d.jpg" % count, dpi = 300)
#       # cv2.imwrite(frames_save_path + "/frame%d.jpg" % count, edges)

#     # if count == 20:
#     #   break  (clip the video )
#   print(count)
 
# if __name__ == '__main__':
#    videos_path = 'D:/Code/Python-DeepLearning/Canny/Video.mp4'
#    frames_save_path = 'D:/Code/Python-DeepLearning/Canny/Frame'
#    # time_interval = 1
#    # videotoframe(videos_path, frames_save_path, time_interval)
#    videotoframe()
#    cv2.destroyAllWindows()
#    cap.release()  

